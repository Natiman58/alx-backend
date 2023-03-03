function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array')
    }
    for (let i = 0; i < jobs.length; i++) {
        const job = queue.create('push_notification_code_3', jobs[i]);
        job.save((err) => {
            if (!err) {
                console.log(`Notification job created ${job.id}`);
            }
        })
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        })
        job.on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`);
        })
        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} progress: ${progress}% complete`);
        })
    }
}
module.exports = createPushNotificationsJobs;