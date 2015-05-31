#!/usr/bin/env ruby

=begin
Find the first four consecutive integers to have four distinct prime factors.
=end

require 'Prime'

a = 2
b = 3
c = 4
d = 5
loop do
  if Prime.prime_division(a).length == 4 and
     Prime.prime_division(b).length == 4 and
     Prime.prime_division(c).length == 4 and
     Prime.prime_division(d).length == 4 and
    puts a
    exit
  end
  a += 1
  b += 1
  c += 1
  d += 1
end
