from starbase import Connection

c = Connection("127.0.0.1", "80000")

ratings = c.table('ratings')

if (ratings.exists()):
    print("Dropping existing ratings table \n")
    ratings.drop()

ratings.create('rating')

print("Parsing the ml-100k ratings data ...\n")
ratingFile = open("/Users/techment/self-learning/data-engineering/HadoopCourse/ml-100k/u.data", "r")

batch = ratings.batch()

for line in ratingFile:
    (userID, movieID, rating, timestamp) = line.split()
    batch.update(userID, { 'rating': { movieID: rating } })

ratingFile.close()

print("Committing ratings data to HBase via REST service \n")
batch.commit(finalize=True)
