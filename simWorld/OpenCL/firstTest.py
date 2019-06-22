import pyopencl as cl
import numpy as np

code = open('kernel.cl').read()

platforms = cl.get_platforms()
cntxt = cl.Context(dev_type=cl.device_type.ALL,
                   properties=[(cl.context_properties.PLATFORM,
                                platforms[0])])
queue = cl.CommandQueue(cntxt)

n = 1000000
# Create the data for computation
num1 = np.array(range(n), dtype=np.int32)
num2 = np.array(range(n), dtype=np.int32)
out= np.empty(num1.shape, dtype=np.int32)

# Create device buffers for inputs
num1_buf = cl.Buffer(cntxt, cl.mem_flags.READ_ONLY |
                     cl.mem_flags.COPY_HOST_PTR, hostbuf=num1)
num2_buf = cl.Buffer(cntxt, cl.mem_flags.READ_ONLY |
                     cl.mem_flags.COPY_HOST_PTR, hostbuf=num2)

# Create device buffer for output
out_buf = cl.Buffer(cntxt, cl.mem_flags.WRITE_ONLY, out.nbytes)

# Build the kernel
bld = cl.Program(cntxt, code).build()

# Launch the kernel
launch = bld.frst_prog(queue, num1.shape, None, num1_buf, num2_buf, out_buf)

# Wait until the processing completes
launch.wait()
cl.enqueue_copy(queue, out, out_buf)

print("Number 1: " + str(num1))
print("Number 2: " + str(num2))
print("Out: " + str(out))
