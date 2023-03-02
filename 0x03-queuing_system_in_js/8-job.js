const queue = require('kue');


function createPushNotificationsJobs(jobs, queue) {
    if (!jobs) {
        throw new Error('Jobs is not an array')
    }
    for (let i = 0; i < jobs.length; i++) {
        const job = queue.create('push_notification_code_3', jobs[i])
            .save((err) => {
                if (!err) {
                    console.log(`Notification job created ${job.id}`);
                }
            })
            .on('complete', () => {
                console.log(`Notification job ${job.id} completed`);
            })
            .on('failed', (err) => {
                console.log(`Notification job ${job.id} failed: ${err}`);
            })
            .on('progress', (progress) => {
                console.log(`Notification job ${job.id} progress: ${progress}% complete`);
            })
    }
}
module.exports = createPushNotificationsJobs;