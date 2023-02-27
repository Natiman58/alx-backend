import redis from 'redis';

const client = redis.createClient();

// create a hash table using the key "HolbertonSchools"
client.hset("HolbertonSchools", "Portland", 50, "Seattle", 80, "New York", 20, "Bogota", 20, "Cali", 40, "Paris", 2, redis.print);

// when client is connected to Redis
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// get all the filds value pairs with the key
client.hgetall("HolbertonSchools", (error, value) => {
    if (error) throw error;
    console.log(value);
});

// when there is error on connecting to Redis
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});