from nose import with_setup
from nose.tools import assert_equals
from lettuce import *


@step('I have (\d+)')
def have_a_number(step, number):
	world.number = int(number)

@step('I compute 1+1 sum')
def compute_its_sum(step):
        world.number = world.number + 1

@step('I see (\d+)')
def check_number(step, expected):
        expected = int(expected)

	def setup():
		pass

	def teardown():
		pass

	@with_setup(setup, teardown)
	def test1():
		assert_equals(world.number, expected)


