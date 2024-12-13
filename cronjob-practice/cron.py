from crontab import CronTab

cron = CronTab()

job = cron.new(command='py D:\Python\cronjob-practice\code.py', comment="my python crontab")

job.minute.every(1)

cron.write()

print("Cronjob added successfully!")

print("Current cron jobs:")
for job in cron:
    print(job)
