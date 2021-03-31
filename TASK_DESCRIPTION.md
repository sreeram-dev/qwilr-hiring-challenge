# Set up instructions

This app was developed in python 3.8.5

# Intro

Qwilr is pivoting into the farm management business and has begun developing a new app. The last developer has started work on an MVP of the management core modules, but you need to get it running and expand the feature list.

# Starting modules

## farm.py

This is the main module, representing a Farm, which is made up of 0 or more crops.

## crop.py

This is the crop data type that make up the content of the farm

# Running instructions

Run the test suites within the python folder:
`python -m unittest test_stage_1`
and
`python -m unittest test_stage_2`

Running the REPL while developing should just require:
`python`

Once in there can run:
`import farm; import crops`
to pull in the files

# The tasks

## Stage 1

Fix the bugs to get the test cases running correctly

## Stage 2

We're expanding the functionality of the farm manager, adding a sell price to the crops and a maximum size to the farm.

The farm class should be given:
 - an extra method `getTotalSellPrice`
 - an integer on construction to set the farm's maximum size
For example, a farm of maximum size 10 can have 10 corn, or 5 corn and 5 tomatoes, but not 5 corn and 6 tomatoes.

Crops are created with a `sellPrice` field that determines the money made from the crop (per unit in the amount).
