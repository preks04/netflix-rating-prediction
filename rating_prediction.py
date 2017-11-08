import tensorflow as tf


filename_queue = tf.train.string_input_producer(["file1.csv", "file2.csv", "file3.csv"])

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# Default values, in case of empty columns. Also specifies the type of the decoded result.
# todos int32 para que sean mas veloz los calculos (la fecha es un timestamp)
record_defaults = [[1], [1], [1], [1]]
MovieIDs, CustomerID, Rating, Date = tf.decode_csv(value, record_defaults=record_defaults)
features = tf.stack([CustomerID, Rating, Date])

with tf.Session() as sess:
    # cola de procesamiento de los archivos
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    for i in range(1200):
        example, label = sess.run([features, MovieIDs])

    estimator = tf.estimator.Estimator.LinearClassifier(
        feature_columns=[CustomerID, Rating, Date],
    )
    estimator.train(input_fn=features, steps=2000)

    coord.request_stop()
    coord.join(threads)
