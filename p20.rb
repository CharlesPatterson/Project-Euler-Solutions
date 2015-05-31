#!/usr/bin/env ruby

=begin
Find the sum of the digits in the number 100!
=end

class Integer
  def factorial
    n = self.to_i
    return 1 if n.zero?
    1.upto(n).inject(:*)
  end
end

puts 100.factorial.to_s.each_char.reduce(0) {|sum,c| sum + c.to_i}
