#!/usr/bin/env ruby

=begin
Calculates the sum of the digits of the number 2**1000.
=end

puts (2**1000).to_s.each_char.reduce(0) {|s,c| s + c.to_i}
