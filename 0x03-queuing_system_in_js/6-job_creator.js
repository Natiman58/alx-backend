const kue = require('kue');

// create a kue queue and set it's redis backend
const queue = kue.createQueue();

// create a job data
const jobData = {
    phoneNumber: '13456987',
    message: 'Hello World',
}

// create the job
const job = queue.create('push_notification_code', jobData).save((err) => {
    if (err) {
        console.log('Notification job failed')
    } else {
        console.log(`Notification job created ${job.id}`)
    }
});

// on completion
job.on('complete', () => {
    console.log('Notification job completed');
});

// on failure
job.on('failed', (err) => {
    console.log('Notification job failed');
});