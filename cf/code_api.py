import hashlib, time, random, requests

# Replace with your details
api_key = "0508392b1f98ac919aec815a935f89e34d94e097"
api_secret = "10aea9bc5b5047f11f7f4ecb61dc24b2bd33ec03"

method = "user.friends"
params = "onlyOnline=false"

rand = random.randint(100000, 999999)
current_time = int(time.time())

# Required by Codeforces API: construct signature
sig_str = f"{rand}/{method}?apiKey={api_key}&{params}&time={current_time}#{api_secret}"
api_sig = hashlib.sha512(sig_str.encode()).hexdigest()

url = f"https://codeforces.com/api/{method}?apiKey={api_key}&{params}&time={current_time}&apiSig={rand}{api_sig}"

response = requests.get(url).json()
print(response)
