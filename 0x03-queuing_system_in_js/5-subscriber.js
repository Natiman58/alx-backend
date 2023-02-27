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

// subscribe to the channel (holberton sch...)
client.subscribe('holberton school channel');

// listen for a message and print it out
client.on('message', (err, msg) => {
    if (msg === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.end(true);
    }
    console.log(msg);
});