from tensorflow.keras import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Flatten, Dense, Dropout


def model_arch():
    classes_count = 3

    base_model = MobileNetV2(weights='imagenet', 
                             include_top=False, 
                             input_shape=(224, 224, 3))

    head_model = base_model.output
    head_model = Flatten()(head_model)
    head_model = Dropout(0.1)(head_model)
    head_model = Dense(128, activation='relu', kernel_initializer="he_normal")(head_model)
    head_model = Dropout(0.1)(head_model)
    head_model = Dense(64, activation='relu', kernel_initializer="he_normal")(head_model)
    head_model = Dropout(0.1)(head_model)
    head_model = Dense(32, activation='relu', kernel_initializer="he_normal")(head_model)
    head_model = Dense(classes_count, activation='softmax')(head_model)

    ##### Place the head model on top of the base model #######
    model = Model(inputs=base_model.input, outputs=head_model)
    ###########################################################
    
    return model