import jax
import jax.numpy as jnp

print(jax.device_count())

if jax.process_count() > 1:
  # Make sure all hosts stay up until the end of main.
  print('Waiting for all hosts in a slice to complete')
  x = jnp.ones([jax.local_device_count()])
  x = jax.device_get(jax.pmap(lambda x: jax.lax.psum(x, 'i'), 'i')(x))
  assert x[0] == jax.device_count()
  print('Job completed')
else:
  print('Running on a single device')


