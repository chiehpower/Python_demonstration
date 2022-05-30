import redis
r = redis.Redis(host='0.0.0.0', port=6379)
print(r)

# Scenarios: There are many users who request to
# use the redis for storing the results.

userA = 'admin'
userB = 'userB'

r.setnx(userA, 700)
r.setnx(userB, 0)

print(r.get(userA))
print(r.get(userB))
for i in range(15):
    print("i", i)
    r.incr(userA, amount=1)
    r.incr(userB, amount=1)
    print(r.get(userA))
    print(r.get(userB))
    print("---")

print("Reset")

# r.getset(userA, 800)
r.getset(userB, 100)
print(r.get(userB))
