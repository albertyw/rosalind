symbols = "L F O R V U H A T D"
length = 2

def create_collection(symbols, length)
  return symbols if length == 1
  collection = symbols.map do |symbol|
    children = create_collection(symbols, length-1)
    children = children.map{|s| symbol + s}
    children
  end
  collection.flatten!
  return collection
end

symbols = symbols.split(' ')
collection = create_collection(symbols, length)
collection.map{|c| print c+"\n"}
