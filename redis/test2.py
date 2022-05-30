import redis
import random
r = redis.Redis(host='0.0.0.0', port=6379, decode_responses=True, db=5)
# print(r)

user = 'user'
project_id = 1
state_id = 5
job_id = random.randint(100000, 1000000)

### Stored list.
## project_id : find which project users use.
## state_id : to get the rule from state_id.

# r.hset("state_id", "project_id", project_id)


# # print("State id: ", r.hkeys("state_id"))

# print("Project id: ", r.hget("state_id", "project_id")) 

# # print("hmget ", r.hmget("state_id", "state_id", "job_id")) 

# r.hsetnx("state_id", "job_id", job_id) 
# print("Job id: ", r.hget("state_id", "job_id"))

# r.delete("state_id")

r.hmset(state_id, {"project_id": project_id, "job_id": job_id})
print(r.hmget(state_id, "project_id"))
# print(r.hget(5, "project_id"))

# r.flushdb()

####
rule = [{"order": 0, "title": "If (Colombia > 1 )"}, {"order": 1, "title": "Or (Colombia > 1 )"}]

num = len(rule)
st = {"project_id": project_id, "rule": num}
if num > 0:
    for i in range(num):
        for ii in rule:
            if ii['order'] == i:
                st['rule_' + str(i)] = ii['title']

if not r.exists(state_id):
    r.hmset(state_id, st)
else:
    if r.hget(state_id, "project_id") == project_id:
        pass
    else:
        r.hmset(state_id, st)

# print(r.hmget(state_id, "project_id"))

print(r.hget(state_id, "project_id"))
print(r.hget(state_id, "rule"))
print(r.hget(state_id, "rule_0"))
