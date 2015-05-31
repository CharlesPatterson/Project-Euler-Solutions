#!/usr/bin/env ruby

=begin
Find the sum of all the primes below 2000000.
=end

require 'Prime'
puts Prime.take_while { |p| p < 2000000 }.reduce(0) {|sum,p| sum + p}
