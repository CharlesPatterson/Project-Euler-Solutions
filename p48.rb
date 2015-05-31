#!/usr/bin/env ruby

=begin
Find the last ten digits of the series 1^1 + 2^2 + ... + 1000^1000.
=end

n = (1..1000).reduce(0) { |s, t| s + t**t }
puts n.to_s[-10,10]
