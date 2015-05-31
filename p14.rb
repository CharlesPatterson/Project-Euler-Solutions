#!/usr/bin/env ruby

=begin
Find the generator for the longest Collatz sequence under 1,000,000.

Collatz Sequence:
n -> n/2  (n is even)
n -> 3n+1 (n is odd)
=end

def trivial_inject(keys, values)
  h = {}
  (0..keys.size-1).each { |k| h[keys[k]] = values[k] }
  h
end

def collatz_sequence(n, cache)
  stack = []
  if n == 1
    return 1
  else
    size = 0
    while n > 1
      if cache.has_key? n then
        big_c = stack.size+1+cache[n]
        small_c = 2+cache[n]
        cache.merge!(trivial_inject(stack, (big_c).downto(small_c).to_a))
        return cache[n]
      end
      stack << n
      n = (n % 2 == 0) ? n / 2 : 3*n + 1
      size += 1
    end
    cache.merge!(trivial_inject(stack, (stack.size+1).downto(2).to_a))
    return size
  end
end

def max_collatz(n)
  max = -1
  max_generator = -1
  cache = {}
  (1..n).each do |i|
    puts "**** #{i} ****"
    size = collatz_sequence(i, cache)
    if size > max then 
      max = size
      max_generator = i
    end
  end  
  max_generator
end

puts max_collatz(1000000)
