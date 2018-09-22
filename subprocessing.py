import subprocess


ping_args = ["ping", "-c", "1", "-s", "1", "-W", "1"]
address = '8.8.8.8'

ping = subprocess.Popen(ping_args + [address], stdout = subprocess.PIPE, stderr = subprocess.PIPE )

out, error = ping.communicate()
print out
print error
print ping.returncode


# Or you can also do
# result = subprocess.call(ping_args+ [address])
# print result