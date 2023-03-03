const createPushNotificationsJobs = require('./8-job')
const queue = require('kue').createQueue();
const expect = require('chai').expect;

describe('createPushNotificationsJobs', function() {
    before(function() {
        queue.testMode.enter();
    });

    afterEach(function() {
        queue.testMode.clear();
    });

    after(function() {
        queue.testMode.exit()
    });

    it('adds jobs to the queue', function() {
        const jobs = [
            { phoneNumber: '123-456-7890', message: 'Test message 1' },
            { phoneNumber: '123-456-7891', message: 'Test message 2' },
            { phoneNumber: '123-456-7892', message: 'Test message 3' }
        ];
        createPushNotificationsJobs(jobs, queue);

        // assert the jobs are added to the queue
        expect(queue.testMode.jobs.length).to.equal(3);

        // checks each job has the correct type and data
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    });

    it('throws an error if the job is not and array', function() {
        const jobs = 'not an array';
        expect(() => createPushNotificationsJobs(jobs, queue)).to.throw('Jobs is not an array');
    });
});