#!/usr/bin/env ruby

=begin
Finds the first term in the Fibonacci sequence to contain 1000 digits.
=end

class Integer
  def digits
    self.to_s.length
  end
end

def fibonacci
  Enumerator.new do |enum|
    p = 0
    c = 1
    loop do
      enum.yield c
      p,c = c,p+c
    end
  end
end

puts fibonacci.find_index { |i| i.digits == 1000 } + 1
