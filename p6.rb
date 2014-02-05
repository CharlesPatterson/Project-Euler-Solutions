#!/usr/bin/env ruby

=begin
Find the difference between the square of the sum of the first n natural numbers and the sum of the squares.

Other useful math functions defined here too.
=end

def sum_to(n)
  (1..n).reduce(0) do |sum, value|
    sum + value
  end
end

def square_of_sum(n)
  sum_to(n)**2
end

def sum_of_powers(n, p)
  (1..n).reduce(0) do |sum, value|
    sum + value**p
  end
end

def sum_of_squares(n)
  sum_of_powers(n, 2)
end

def sum_of_cubes(n)
  sum_of_powers(n, 3)
end

puts (square_of_sum(100) - sum_of_squares(100)).abs
