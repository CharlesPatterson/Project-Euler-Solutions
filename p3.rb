#!/usr/bin/env ruby

=begin
Finds the largest prime factor of 600851475143.
=end

require 'Prime'

puts Prime.take_while { |p| p < 600851475143 }
