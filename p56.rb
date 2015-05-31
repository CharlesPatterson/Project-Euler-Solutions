#!/usr/bin/env ruby

=begin
Calculates the maximum digital sum for natural numbers of the form, a**b, where a, b < 100, 
=end

class Integer
  def digit_sum
    self.to_s.each_char.reduce(0) {|s,c| s + c.to_i}
  end
end

max_sum = -1
(0..99).each do |i|
  (0..99).each do |j|
    sum = (i**j).digit_sum
    if sum > max_sum then
      max_sum = sum
    end
  end
end

puts max_sum
