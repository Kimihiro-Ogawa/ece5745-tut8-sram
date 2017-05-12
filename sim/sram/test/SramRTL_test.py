#=======================================================================
# SramRTL_test.py
#=======================================================================
# Unit Tests for SRAM RTL model

import pytest
import random

from pymtl        import *
from pclib.test   import run_test_vector_sim
from sram.SramRTL import SramRTL

#-------------------------------------------------------------------------
# SRAM to be tested
#-------------------------------------------------------------------------
# If you add a new SRAM, make sure add it here to test it.

sram_configs = [ (16, 32), (32, 256), (128, 256) ]

# ''' TUTORIAL TASK '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Add (64,64) configuration to sram_configs
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#-----------------------------------------------------------------------
# Directed test for 16x32 SRAM
#-----------------------------------------------------------------------

def test_direct_16x32( dump_vcd, test_verilog ):
  test_vectors = [ header_str,
    # val,  type,  wben,    idx, wdata, rdata
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 1,     0b11,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0x0000 ],
    [    1, 1,     0b01,     0, 0xbeef, 0x0000 ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0x00ef ],
    [    1, 1,     0b10,     0, 0xefab, 0x00ef ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0xefef ],
    [    1, 1,     0b11,     0, 0x0000, 0xefef ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0x0000 ],
    [    1, 1,     0b11,     0, 0xbeef, 0x0000 ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0xbeef ],
    [    1, 1,     0b11,     0, 0xffff, 0xbeef ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0xffff ],
    [    1, 0,     0b00,   0xf, 0x0000, 0xffff ],
    [    1, 1,     0b11,   0xf, 0xbeef, '?'    ],
    [    1, 0,     0b11,   0xf, 0xcccc, '?'    ],
    [    1, 0,     0b00,   0xf, 0x0000, 0xbeef ],
  ]
  run_test_vector_sim( SramRTL(16, 32), test_vectors, dump_vcd, test_verilog )

#-----------------------------------------------------------------------
# Directed test for 32x256 SRAM
#-----------------------------------------------------------------------

def test_direct_32x256( dump_vcd, test_verilog ):
  test_vectors = [ header_str,
    # val,  type,  wben,    idx,  wdata,      rdata
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 1,  0b1111,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0x00000000 ],
    [    1, 1,  0b0001,     0, 0xdeadbeef, 0x00000000 ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0x000000ef ],
    [    1, 1,  0b0110,     0, 0xabcdefab, 0x000000ef ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0x00cdefef ],
    [    1, 1,  0b1011,     0, 0xff000000, 0x00cdefef ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0xffcd0000 ],
    [    1, 1,  0b1111,     0, 0xdeadbeef, 0xffcd0000 ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0xdeadbeef ],
    [    1, 1,  0b1111,     0, 0xffffffff, 0xdeadbeef ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0xffffffff ],
    [    1, 0,  0b0000,  0xfe, 0x00000000, 0xffffffff ],
    [    1, 1,  0b1111,  0xfe, 0xdeadbeef, '?'        ],
    [    1, 0,  0b1111,  0xfe, 0xbbbbcccc, '?'        ],
    [    1, 0,  0b0000,  0xfe, 0x00000000, 0xdeadbeef ],
  ]
  run_test_vector_sim( SramRTL(32, 256), test_vectors, dump_vcd, test_verilog )

#-----------------------------------------------------------------------
# Directed test for 128x256 SRAM
#-----------------------------------------------------------------------

def test_direct_128x256( dump_vcd, test_verilog ):
  test_vectors = [ header_str,
    # val,  type,  wben,    idx,  wdata,      rdata
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 1,  0b1111,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0x00000000 ],
    [    1, 1,  0b0001,     0, 0xdeadbeef, 0x00000000 ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0x000000ef ],
    [    1, 1,  0b0110,     0, 0xabcdefab, 0x000000ef ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0x00cdefef ],
    [    1, 1,  0b1011,     0, 0xff000000, 0x00cdefef ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0xffcd0000 ],
    [    1, 1,  0b1111,     0, 0xdeadbeef, 0xffcd0000 ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0xdeadbeef ],
    [    1, 1,  0b1111,     0, 0xffffffff, 0xdeadbeef ],
    [    1, 0,  0b0000,     0, 0x00000000, '?'        ],
    [    1, 0,  0b0000,     0, 0x00000000, 0xffffffff ],
    [    1, 0,  0b0000,  0xff, 0x00000000, 0xffffffff ],
    [    1, 1,  0b1111,  0xff, 0xdeadbeef, '?'        ],
    [    1, 0,  0b1111,  0xff, 0xbbbbcccc, '?'        ],
    [    1, 0,  0b0000,  0xff, 0x00000000, 0xdeadbeef ],
  ]
  run_test_vector_sim( SramRTL(128, 256), test_vectors, dump_vcd, test_verilog )

#-----------------------------------------------------------------------
# Directed test for 16x32 SRAM
#-----------------------------------------------------------------------

def test_direct_16x32( dump_vcd, test_verilog ):
  test_vectors = [ header_str,
    # val,  type,  wben,    idx, wdata, rdata
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 1,     0b11,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0x0000 ],
    [    1, 1,     0b01,     0, 0xbeef, 0x0000 ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0x00ef ],
    [    1, 1,     0b10,     0, 0xefab, 0x00ef ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0xefef ],
    [    1, 1,     0b11,     0, 0x0000, 0xefef ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0x0000 ],
    [    1, 1,     0b11,     0, 0xbeef, 0x0000 ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0xbeef ],
    [    1, 1,     0b11,     0, 0xffff, 0xbeef ],
    [    1, 0,     0b00,     0, 0x0000, '?'    ],
    [    1, 0,     0b00,     0, 0x0000, 0xffff ],
    [    1, 0,     0b00,   0xf, 0x0000, 0xffff ],
    [    1, 1,     0b11,   0xf, 0xbeef, '?'    ],
    [    1, 0,     0b11,   0xf, 0xcccc, '?'    ],
    [    1, 0,     0b00,   0xf, 0x0000, 0xbeef ],
  ]
  run_test_vector_sim( SramRTL(16, 32), test_vectors, dump_vcd, test_verilog )

# ''' TUTORIAL TASK '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Add directed test for 64x64 configuration
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#-------------------------------------------------------------------------
# Random testing
#-------------------------------------------------------------------------
# We define the header string here since it is so long. Then reference
# the header string and include a comment to label each of the columns.

header_str = \
  ( "port0_val", "port0_type", "port0_wben",  "port0_idx",
    "port0_wdata", "port0_rdata*" )

def gen_rand_tvec( num_bits = 32, num_words = 256 ):

  rgen = random.Random()
  rgen.seed(0xdeadbeef)

  num_tests = 100

  test_vectors = [ header_str,
    # val, type,  wben,    addr, wdata,      rdata
    [  1,     0,  0b0000,     0, 0x00000000, '?'        ],
    [  1,     0,  0b0000,     0, 0x00000000, '?'        ],
  ]

  wben_all1 = 2**(num_bits/8) - 1

  for i in xrange(num_tests):
    addr  = rgen.randint( 0, num_words-1   )
    wdata = rgen.randint( 0, 2**num_bits-1 )

    #         val, type,  wben,      addr,  wdata, rdata
    vec_wr  = [ 1, 1,     wben_all1, addr,  wdata, '?'   ]
    vec_rd0 = [ 1, 0,     wben_all1, addr,  0x0,   '?'   ]
    vec_rd1 = [ 1, 0,     wben_all1, addr,  0x0,   wdata ]

    test_vectors.append( vec_wr  )
    test_vectors.append( vec_rd0 )
    test_vectors.append( vec_rd1 )

    return test_vectors

#-----------------------------------------------------------------------
# random test
#-----------------------------------------------------------------------

@pytest.mark.parametrize(("num_bits", "num_words"), sram_configs )
def test_random( num_bits, num_words, dump_vcd, test_verilog ):
  run_test_vector_sim( SramRTL(num_bits, num_words),
                       gen_rand_tvec(num_bits, num_words),
                       dump_vcd, test_verilog )

