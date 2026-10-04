x = [0,1,2,3,4,5]
y = [2,6,7,12,13,18]

w = 1
b = 0

learning_rate = 0.01
epsilon = 0.01



def predict(x_value):
    prediction = x_value * w + b
    return prediction

#''' predictions = []
# for i in x:
#     predictions.append(predict(i))
# print("the predictions are", predictions)

# squared_errors = []

# for i in zip(y , predictions):
#     actual, prediction = i
#     error = actual - prediction
#     squared_errors.append(error * error)

# print("The squared errors are", squared_errors)

# mse = sum(squared_errors) / len(squared_errors)
# print("the mse is", mse)'''

def calculate_mse(w, b):
    predictions = []
    for i in x:
        prediction = i * w + b
        predictions.append(prediction)
    squared_errors = []
    for i in zip(y , predictions):
        actual, prediction = i
        error = actual - prediction
        squared_errors.append(error * error)
    mse = sum(squared_errors) / len(squared_errors)
    return mse


#'''OLD CODE
# for i in range(100):
#     old_loss = calculate_mse(w , b)
#     new_loss_w = calculate_mse(w + epsilon, b)
#     new_loss_b = calculate_mse(w, b + epsilon)

#     gradient_w = (new_loss_w - old_loss) / epsilon
#     gradient_b = (new_loss_b - old_loss) / epsilon

#     w = w - (learning_rate * gradient_w)
#     b = b - (learning_rate * gradient_b)
#     if i % 10 == 0:
#       print("step", i)
#       print("the loss is", calculate_mse(w, b))
#       print("w is",w)
#       print("b is", b)
#       print("learning rate is", learning_rate)'''
    

#gradient training

for i in range(1000):   
  total_gradient_w = 0
  total_gradient_b = 0
  
  for x_value, y_value in zip(x, y):
      prediction = w * x_value + b
      error = prediction - y_value
      contribution_w = 2 * error * x_value
      contribution_b = 2 * error
      total_gradient_b += contribution_b
      total_gradient_w += contribution_w

  gradient_w = total_gradient_w / len(x)
  gradient_b = total_gradient_b / len(x)

  w = w - learning_rate * gradient_w
  b = b - learning_rate * gradient_b

  if i % 100 == 0:
      print("STEP IS: ", i)
      print("W is: ", w)
      print("B is: ", b)
      print("MSE is: ", calculate_mse(w, b))