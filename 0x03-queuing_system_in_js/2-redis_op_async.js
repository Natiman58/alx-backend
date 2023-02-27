import redis from 'redis';

// import promisify from utility
const { promisify } = require('util')

// create a Redis client
const client = redis.createClient();

// get the promisified(async) version of client.get function
const getAsync = promisify(client.get).bind(client)

// when client is connected to Redis
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// when there is error on connecting to Redis
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

// add new function
function setNewSchool(schoolName, value) {
    // set the value and print confirmation message with redis.print
    client.SET(schoolName, value, redis.print);
}

// add another function displaySchoolValue
async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName);
    console.log(value)
}


displaySchoolValue('Holberton');

setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');