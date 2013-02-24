inputs = '18174 19945 17670 19919 16382 16398'
inputs = inputs.split(' ')
inputs = [int(s) for s in inputs]

expected = 0.0
expected += inputs[0]
expected += inputs[1]
expected += inputs[2]
expected += inputs[3]*0.75
expected += inputs[4]*0.5
expected += inputs[5]*0

expected *= 2

print expected
