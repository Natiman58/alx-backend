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

// add new function
function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, redis.print);
}

// add another function displaySchoolValue
function displaySchoolValue(schoolName) {
    client.GET(schoolName, (error, value) => {
        if (error) throw error;
        console.log(`${value}`);
    });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');