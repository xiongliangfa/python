from rev_ai import apiclient

# create client
client = apiclient.RevAiAPIClient("02kKwGZct_KjoOdC2a9raV9IY7LFRRme2JcCEE-JGENe-vfTHIdSl-qUT4H_lS8aS9U4URGZQjPPm-3HQB_c6Klfi0fLk")
job = client.send_job_url("D:\\PYTHON\\python\\test\\audio\\New folder\\aud1.mp3")
job_details = client.get_job_details(job.id)
print(job_details)
transcript_json = client.get_transcript_json(job.id)