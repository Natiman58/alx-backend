// import kue lib and create a que instance
const kue = require('kue');
const queue = kue.createQueue();

// a function to send a notification
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs with the name 'push_notification_code' and
// define a callback function to handle each job
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done(); // job completed
});