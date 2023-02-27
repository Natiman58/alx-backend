import redis from 'redis';

// create a Redis client
const client = redis.createClient();


// when client is connected to Redis
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// when there is error on connecting to Redis
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});