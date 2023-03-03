const redis = require('redis');

const express = require('express');
const app = express();
const port = 1245
const { promisify } = require('util');

// connect to redis
const client = redis.createClient();

// promisify redis to get and set methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Define list of products with their details
const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
]

// To get items by id
function getItemById(id) {
    return listProducts.find(item => item.itemId === id);
}

// To reserve the stock by id in redis
async function reserveStockById(itemId, stock) {
    await setAsync(itemId, stock)
}

// Get the reserved stock by id
async function getCurrentReservedStockById(itemId) {
    const reservedStock = await getAsync(itemId);
    return reservedStock ? parseInt(reservedStock) : 0;
}

app.get('/list_products', (req, res) => {
    res.json(listProducts)
})

// the route to get the product details by id
app.get('/list_products/:itemId', async(req, res) => {
    const id = parseInt(req.params.itemId)
    const item = getItemById(id);
    if (!item) {
        res.json({ status: "Product not found" });
        return;
    }
    const currentQuantity = item.initialAvailableQuantity - await getCurrentReservedStockById(id);
    res.json({...item, currentQuantity });

});

// A route to reserve a product by id
app.get('/reserve_product/:itemId', async(req, res) => {
    const id = parseInt(req.params.itemId);
    const item = getItemById(id);
    if (!item) {
        res.json({ status: "Product not found" });
    }
    const currentQuantity = item.initialAvailableQuantity - await getCurrentReservedStockById(id);
    if (currentQuantity < 1) {
        res.json({ status: `Not enough stock available, itemId: ${id}` });
    }
    await reserveStockById(id, 1)
    res.json({ status: `Reservation confirmed, itemId: ${id}` })
})

app.listen(port, () => {
    console.log(`listening on port ${port}`)
});