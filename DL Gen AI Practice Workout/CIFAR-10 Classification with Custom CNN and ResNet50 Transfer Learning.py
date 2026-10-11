import tensorflow as tf
from tensorflow.keras import layers, Sequential
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

#1.load the dataset

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()

#normalise the dataset

X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

print(X_train.shape)

#2. build cnn layers

cnn = Sequential([

layers.Input(shape=(32, 32, 3)),

layers.Conv2D(32, (3,3), activation="relu"),

layers.MaxPooling2D((2,2)),

layers.Conv2D(64, (3,3), activation="relu"),

layers.MaxPooling2D((2,2)), # 3, -1, 4, 5 -> 3x-1x4x5 ->

layers.Flatten(),

layers.Dense(128, activation="relu"),

layers.Dense(10, activation="softmax")

 ])

#3.compile

cnn.compile(
    optimizer = "adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

#4.train the cnn

cnn.fit(
    X_train, y_train, epochs=5, validation_split=0.2
)

#5. test the cnn

test_loss, test_accuracy = cnn.evaluate(X_test, y_test)

print("CNN Test Accuracy: ", test_accuracy)


#6. transfer learning with resnet50

X_train_resized = tf.image.resize(X_train, (224, 224))
X_test_resized = tf.image.resize(X_test, (224, 224))

X_train_resized = preprocess_input(X_train_resized * 255.0)
X_test_resized = preprocess_input(X_test_resized * 255.0)

#7.load the pretrained resnet

base_model = ResNet50(
    weights="imagenet",
    include_top=False,
    input_shape = (224, 224, 3)

)

base_model.trainable = False

#8.create the model

transfer_model = Sequential([

          base_model,
          layers.GlobalAveragePooling2D(),
          layers.Dense(128, activation="relu"),
          layers.Dense(10, activation="softmax")
])

#9.compile

transfer_model.compile(

    optimizer = "adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

#10. train

transfer_model.fit(X_train_resized, y_train, epochs=3, validation_split=0.2)

#11. test

test_loss, test_accuracy = transfer_model.evaluate(X_test_resized, y_test)

print("Model Test Accuracy: ", test_accuracy)