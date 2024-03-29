from builtins import range
import numpy as np


def affine_forward(x, w, b):
    """
    Computes the forward pass for an affine (fully-connected) layer.

    The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
    examples, where each example x[i] has shape (d_1, ..., d_k). We will
    reshape each input into a vector of dimension D = d_1 * ... * d_k, and
    then transform it to an output vector of dimension M.

    Inputs:
    - x: A numpy array containing input data, of shape (N, d_1, ..., d_k)
    - w: A numpy array of weights, of shape (D, M)
    - b: A numpy array of biases, of shape (M,)

    Returns a tuple of:
    - out: output, of shape (N, M)
    - cache: (x, w, b)
    """
    out = None
    ###########################################################################
    # TODO: Implement the affine forward pass. Store the result in out. You   #
    # will need to reshape the input into rows.                               #
    ###########################################################################
    N = x.shape[0]
    x_re = x.reshape(N, -1) # dimensions d_1, ..., d_k are in one dimension
    out = x_re.dot(w) + b
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, w, b)
    return out, cache


def affine_backward(dout, cache):
    """
    Computes the backward pass for an affine layer.

    Inputs:
    - dout: Upstream derivative, of shape (N, M)
    - cache: Tuple of:
      - x: Input data, of shape (N, d_1, ... d_k)
      - w: Weights, of shape (D, M)

    Returns a tuple of:
    - dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
    - dw: Gradient with respect to w, of shape (D, M)
    - db: Gradient with respect to b, of shape (M,)
    """
    x, w, b = cache
    dx, dw, db = None, None, None
    ###########################################################################
    # TODO: Implement the affine backward pass.                               #
    ###########################################################################
    # w
    # ----+
    # dw   \
    #      (*)----+
    # x    /       \
    # ----+         \   out
    # dx            (+)------
    #               /   dout
    # b            /
    # ------------+
    # db    
    
    N = x.shape[0]
    x_re = x.reshape(N, -1)
    
    db = np.sum(dout, axis=0)    
    dx = dout.dot(w.T).reshape(x.shape)
    dw = x_re.T.dot(dout)
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dw, db


def relu_forward(x):
    """
    Computes the forward pass for a layer of rectified linear units (ReLUs).

    Input:
    - x: Inputs, of any shape

    Returns a tuple of:
    - out: Output, of the same shape as x
    - cache: x
    """
    out = None
    ###########################################################################
    # TODO: Implement the ReLU forward pass.                                  #
    ###########################################################################
    out = np.maximum(0, x)
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = x
    return out, cache


def relu_backward(dout, cache):
    """
    Computes the backward pass for a layer of rectified linear units (ReLUs).

    Input:
    - dout: Upstream derivatives, of any shape
    - cache: Input x, of same shape as dout

    Returns:
    - dx: Gradient with respect to x
    """
    dx, x = None, cache
    ###########################################################################
    # TODO: Implement the ReLU backward pass.                                 #
    ###########################################################################
    dx = (x > 0) * dout
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx


def batchnorm_forward(x, gamma, beta, bn_param):
    """
    Forward pass for batch normalization.

    During training the sample mean and (uncorrected) sample variance are
    computed from minibatch statistics and used to normalize the incoming data.
    During training we also keep an exponentially decaying running mean of the
    mean and variance of each feature, and these averages are used to normalize
    data at test-time.

    At each timestep we update the running averages for mean and variance using
    an exponential decay based on the momentum parameter:

    running_mean = momentum * running_mean + (1 - momentum) * sample_mean
    running_var = momentum * running_var + (1 - momentum) * sample_var

    Note that the batch normalization paper suggests a different test-time
    behavior: they compute sample mean and variance for each feature using a
    large number of training images rather than using a running average. For
    this implementation we have chosen to use running averages instead since
    they do not require an additional estimation step; the torch7
    implementation of batch normalization also uses running averages.

    Input:
    - x: Data of shape (N, D)
    - gamma: Scale parameter of shape (D,)
    - beta: Shift paremeter of shape (D,)
    - bn_param: Dictionary with the following keys:
      - mode: 'train' or 'test'; required
      - eps: Constant for numeric stability
      - momentum: Constant for running mean / variance.
      - running_mean: Array of shape (D,) giving running mean of features
      - running_var Array of shape (D,) giving running variance of features

    Returns a tuple of:
    - out: of shape (N, D)
    - cache: A tuple of values needed in the backward pass
    """
    mode = bn_param['mode']
    eps = bn_param.get('eps', 1e-5)
    momentum = bn_param.get('momentum', 0.9)

    N, D = x.shape
    running_mean = bn_param.get('running_mean', np.zeros(D, dtype=x.dtype))
    running_var = bn_param.get('running_var', np.zeros(D, dtype=x.dtype))

    out, cache = None, None
    if mode == 'train':
        #######################################################################
        # TODO: Implement the training-time forward pass for batch norm.      #
        # Use minibatch statistics to compute the mean and variance, use      #
        # these statistics to normalize the incoming data, and scale and      #
        # shift the normalized data using gamma and beta.                     #
        #                                                                     #
        # You should store the output in the variable out. Any intermediates  #
        # that you need for the backward pass should be stored in the cache   #
        # variable.                                                           #
        #                                                                     #
        # You should also use your computed sample mean and variance together #
        # with the momentum variable to update the running mean and running   #
        # variance, storing your result in the running_mean and running_var   #
        # variables.                                                          #
        #######################################################################
        
        ## This is how I've done it (works):
        ## Formulas from 'Batch Normalization: ... ' by Sergey Ioffe and Christian Szegedy:
        ## https://arxiv.org/pdf/1502.03167.pdf
        ## Mini-batch mean and variance
        #sample_mean = np.mean(x, axis=0)
        #sample_var = np.var(x, axis=0)
        ## Normalize
        #x_norm = (x - sample_mean) / np.sqrt(sample_var + eps)
        ## Outputs
        #out = gamma * x_norm + beta
        #cache = ()
        ## Update running mean and var
        #running_mean = momentum * running_mean + (1 - momentum) * sample_mean
        #running_var = momentum * running_var + (1 - momentum) * sample_var
        
        # Taken from cthorey's solution:
        # https://github.com/cthorey/CS231/blob/master/assignment2/cs231n/layers.py#L154
        # Step 1 - shape of mu (D,)
        mu = 1 / float(N) * np.sum(x, axis=0)
        # Step 2 - shape of var (N,D)
        xmu = x - mu
        # Step 3 - shape of carre (N,D)
        carre = xmu**2
        # Step 4 - shape of var (D,)
        var = 1 / float(N) * np.sum(carre, axis=0)
        # Step 5 - Shape sqrtvar (D,)
        sqrtvar = np.sqrt(var + eps)
        # Step 6 - Shape invvar (D,)
        invvar = 1. / sqrtvar
        # Step 7 - Shape va2 (N,D)
        va2 = xmu * invvar
        # Step 8 - Shape va3 (N,D)
        va3 = gamma * va2
        # Step 9 - Shape out (N,D)
        out = va3 + beta

        running_mean = momentum * running_mean + (1.0 - momentum) * mu
        running_var = momentum * running_var + (1.0 - momentum) * var

        cache = (mu, xmu, carre, var, sqrtvar, invvar,
                 va2, va3, gamma, beta, x, bn_param)
        
        #######################################################################
        #                           END OF YOUR CODE                          #
        #######################################################################
    elif mode == 'test':
        #######################################################################
        # TODO: Implement the test-time forward pass for batch normalization. #
        # Use the running mean and variance to normalize the incoming data,   #
        # then scale and shift the normalized data using gamma and beta.      #
        # Store the result in the out variable.                               #
        #######################################################################
        
        mu = running_mean
        var = running_var
        # Normalize
        x_norm = (x - running_mean) / np.sqrt(running_var + eps)
        # Output
        out = gamma * x_norm + beta
        cache = (mu, var, gamma, beta, bn_param)
        
        #######################################################################
        #                          END OF YOUR CODE                           #
        #######################################################################
    else:
        raise ValueError('Invalid forward batchnorm mode "%s"' % mode)

    # Store the updated running means back into bn_param
    bn_param['running_mean'] = running_mean
    bn_param['running_var'] = running_var

    return out, cache


def batchnorm_backward(dout, cache):
    """
    Backward pass for batch normalization.

    For this implementation, you should write out a computation graph for
    batch normalization on paper and propagate gradients backward through
    intermediate nodes.

    Inputs:
    - dout: Upstream derivatives, of shape (N, D)
    - cache: Variable of intermediates from batchnorm_forward.

    Returns a tuple of:
    - dx: Gradient with respect to inputs x, of shape (N, D)
    - dgamma: Gradient with respect to scale parameter gamma, of shape (D,)
    - dbeta: Gradient with respect to shift parameter beta, of shape (D,)
    """
    dx, dgamma, dbeta = None, None, None
    ###########################################################################
    # TODO: Implement the backward pass for batch normalization. Store the    #
    # results in the dx, dgamma, and dbeta variables.                         #
    ###########################################################################
    
    # Taken from cthorey's solution:
    # https://github.com/cthorey/CS231/blob/master/assignment2/cs231n/layers.py#L233
    
    mu, xmu, carre, var, sqrtvar, invvar, va2, va3, gamma, beta, x, bn_param = cache
    eps = bn_param.get('eps', 1e-5)
    N, D = dout.shape

    # Backprop Step 9
    dva3 = dout
    dbeta = np.sum(dout, axis=0)
    # Backprop step 8
    dva2 = gamma * dva3
    dgamma = np.sum(va2 * dva3, axis=0)
    # Backprop step 7
    dxmu = invvar * dva2
    dinvvar = np.sum(xmu * dva2, axis=0)
    # Backprop step 6
    dsqrtvar = -1. / (sqrtvar**2) * dinvvar
    # Backprop step 5
    dvar = 0.5 * (var + eps)**(-0.5) * dsqrtvar
    # Backprop step 4
    dcarre = 1 / float(N) * np.ones((carre.shape)) * dvar
    # Backprop step 3
    dxmu += 2 * xmu * dcarre
    # Backprop step 2
    dx = dxmu
    dmu = - np.sum(dxmu, axis=0)
    # Basckprop step 1
    dx += 1 / float(N) * np.ones((dxmu.shape)) * dmu
    
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return dx, dgamma, dbeta


def batchnorm_backward_alt(dout, cache):
    """
    Alternative backward pass for batch normalization.

    For this implementation you should work out the derivatives for the batch
    normalizaton backward pass on paper and simplify as much as possible. You
    should be able to derive a simple expression for the backward pass.

    Note: This implementation should expect to receive the same cache variable
    as batchnorm_backward, but might not use all of the values in the cache.

    Inputs / outputs: Same as batchnorm_backward
    """
    dx, dgamma, dbeta = None, None, None
    ###########################################################################
    # TODO: Implement the backward pass for batch normalization. Store the    #
    # results in the dx, dgamma, and dbeta variables.                         #
    #                                                                         #
    # After computing the gradient with respect to the centered inputs, you   #
    # should be able to compute gradients with respect to the inputs in a     #
    # single statement; our implementation fits on a single 80-character line.#
    ###########################################################################
    
    # Taken from cthorey's solution:
    # https://github.com/cthorey/CS231/blob/master/assignment2/cs231n/layers.py#L294
    
    mu, xmu, carre, var, sqrtvar, invvar, va2, va3, gamma, beta, x, bn_param = cache
    eps = bn_param.get('eps', 1e-5)
    N, D = dout.shape

    dbeta = np.sum(dout, axis=0)
    dgamma = np.sum((x - mu) * (var + eps)**(-1. / 2.) * dout, axis=0)
    dx = (1. / N) * gamma * (var + eps)**(-1. / 2.) * (N * dout - np.sum(dout, axis=0)
                                                       - (x - mu) * (var + eps)**(-1.0) * np.sum(dout * (x - mu), axis=0))
    
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return dx, dgamma, dbeta


def dropout_forward(x, dropout_param):
    """
    Performs the forward pass for (inverted) dropout.

    Inputs:
    - x: Input data, of any shape
    - dropout_param: A dictionary with the following keys:
      - p: Dropout parameter. We drop each neuron output with probability p.
      - mode: 'test' or 'train'. If the mode is train, then perform dropout;
        if the mode is test, then just return the input.
      - seed: Seed for the random number generator. Passing seed makes this
        function deterministic, which is needed for gradient checking but not
        in real networks.

    Outputs:
    - out: Array of the same shape as x.
    - cache: tuple (dropout_param, mask). In training mode, mask is the dropout
      mask that was used to multiply the input; in test mode, mask is None.
    """
    p, mode = dropout_param['p'], dropout_param['mode']
    if 'seed' in dropout_param:
        np.random.seed(dropout_param['seed'])

    mask = None
    out = None

    if mode == 'train':
        #######################################################################
        # TODO: Implement training phase forward pass for inverted dropout.   #
        # Store the dropout mask in the mask variable.                        #
        #######################################################################
        
        # I inverted the dropout p to be 1-p. Using 1-p is actual dropout, 
        # otherwise it is 'keepin'. p is the percentage of values kept.
        mask = (np.random.rand(*x.shape) < (1-p)) / (1-p)
        out = x * mask
        
        #######################################################################
        #                           END OF YOUR CODE                          #
        #######################################################################
    elif mode == 'test':
        #######################################################################
        # TODO: Implement the test phase forward pass for inverted dropout.   #
        #######################################################################
        
        mask = None
        out = x        
    
        #######################################################################
        #                            END OF YOUR CODE                         #
        #######################################################################

    cache = (dropout_param, mask)
    out = out.astype(x.dtype, copy=False)

    return out, cache


def dropout_backward(dout, cache):
    """
    Perform the backward pass for (inverted) dropout.

    Inputs:
    - dout: Upstream derivatives, of any shape
    - cache: (dropout_param, mask) from dropout_forward.
    """
    dropout_param, mask = cache
    mode = dropout_param['mode']

    dx = None
    if mode == 'train':
        #######################################################################
        # TODO: Implement training phase backward pass for inverted dropout   #
        #######################################################################
        
        dx  = dout * mask
        
        #######################################################################
        #                          END OF YOUR CODE                           #
        #######################################################################
    elif mode == 'test':
        dx = dout
    return dx


def conv_forward_naive(x, w, b, conv_param):
    """
    A naive implementation of the forward pass for a convolutional layer.

    The input consists of N data points, each with C channels, height H and
    width W. We convolve each input with F different filters, where each filter
    spans all C channels and has height HH and width HH.

    Input:
    - x: Input data of shape (N, C, H, W)
    - w: Filter weights of shape (F, C, HH, WW)
    - b: Biases, of shape (F,)
    - conv_param: A dictionary with the following keys:
      - 'stride': The number of pixels between adjacent receptive fields in the
        horizontal and vertical directions.
      - 'pad': The number of pixels that will be used to zero-pad the input.

    Returns a tuple of:
    - out: Output data, of shape (N, F, H', W') where H' and W' are given by
      H' = 1 + (H + 2 * pad - HH) / stride
      W' = 1 + (W + 2 * pad - WW) / stride
    - cache: (x, w, b, conv_param)
    """
    out = None
    ###########################################################################
    # TODO: Implement the convolutional forward pass.                         #
    # Hint: you can use the function np.pad for padding.                      #
    ###########################################################################
    
    # Unpack sizes
    N, C, H, W = x.shape
    F, _, HH, WW = w.shape
    P = conv_param['pad']
    S = conv_param['stride']        
    Hout = 1 + (H + 2 * P - HH) / S
    Wout = 1 + (W + 2 * P - WW) / S
    
    # Hout and Wout are floats after /
    if all([int(Hout) == Hout, int(Wout) == Wout]):
        Hout = int(Hout)
        Wout = int(Wout)
    else:
        raise ValueError("Non-integer output size: {}x{}".format(Hout, Wout))
        
    # Pad: 0s added to   N      C      H      W   axis, to the (beginning, end)
    x_pad = np.pad(x, ((0,0), (0,0), (P,P), (P,P)), 'constant', constant_values=0)
    
    # Compute layer output
    out = np.zeros((N, F, Hout, Wout))
    for n in range(N):
        img = x_pad[n, ...]  # One image (C, H, W)
        for f in range(F):
            filter = w[f, ...]  # One filter layer (C, HH, WW)
            bf = b[f]           # Bias scalar (1)
            for ho in range(Hout):
                for wo in range(Wout):
                    # Img slice through all channels with space dims equal to filter space dims
                    img_deep_slice = img[:, ho*S : ho*S+HH, wo*S : wo*S+WW]  # (C, HH, WW)
                    # Dot product image slice with filter layer and add bias
                    out[n, f, ho, wo] = np.sum(img_deep_slice * filter) + bf
    
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, w, b, conv_param)
    return out, cache


def conv_backward_naive(dout, cache):
    """
    A naive implementation of the backward pass for a convolutional layer.

    Inputs:
    - dout: Upstream derivatives.
    - cache: A tuple of (x, w, b, conv_param) as in conv_forward_naive

    Returns a tuple of:
    - dx: Gradient with respect to x
    - dw: Gradient with respect to w
    - db: Gradient with respect to b
    """
    dx, dw, db = None, None, None
    ###########################################################################
    # TODO: Implement the convolutional backward pass.                        #
    ###########################################################################
    
    # Adapted from lightaime's solutions:
    # https://github.com/lightaime/cs231n/blob/master/assignment2/cs231n/layers.py#L449
    # Backpropagation of convolution is also a convolution, see:
    # http://cs231n.github.io/convolutional-networks/
  
    # Unpack variables
    x, w, b, conv_param = cache  
    N, C, H, W = x.shape
    F, _, HH, WW = w.shape
    S = conv_param['stride']
    P = conv_param['pad']
    Hout = 1 + (H + 2 * P - HH) / S
    Wout = 1 + (W + 2 * P - WW) / S
    
    # Hout and Wout are floats after /
    if all([int(Hout) == Hout, int(Wout) == Wout]):
        Hout = int(Hout)
        Wout = int(Wout)
    else:
        raise ValueError("Non-integer output size: {}x{}".format(Hout, Wout))
  
    # Pad: 0s added to   N      C      H      W   axis, to the (beginning, end)
    x_pad = np.pad(x, ((0,0), (0,0), (P,P), (P,P)), 'constant', constant_values=0)
    
    dx = np.zeros_like(x)
    dx_pad = np.zeros_like(x_pad)
    dw = np.zeros_like(w)
    db = np.zeros_like(b)
  
    # Compute gradients
    db = np.sum(dout, axis = (0,2,3))
        
    for i in range(Hout):
        for j in range(Wout):
            x_pad_sub = x_pad[:, :, i*S:i*S+HH, j*S:j*S+WW]
            for k in range(F): # compute dw
                dw[k ,: ,: ,:] += \
                  np.sum(x_pad_sub * (dout[:, k, i, j])[:, None, None, None], axis=0)
            for n in range(N): # compute dx_pad (convolution)
                dx_pad[n, :, i*S:i*S+HH, j*S:j*S+WW] += \
                  np.sum((w[:, :, :, :] * (dout[n, :, i, j])[:,None ,None, None]), axis=0)
    dx = dx_pad[:,:,P:-P,P:-P]
    
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dw, db


def max_pool_forward_naive(x, pool_param):
    """
    A naive implementation of the forward pass for a max pooling layer.

    Inputs:
    - x: Input data, of shape (N, C, H, W)
    - pool_param: dictionary with the following keys:
      - 'pool_height': The height of each pooling region
      - 'pool_width': The width of each pooling region
      - 'stride': The distance between adjacent pooling regions

    Returns a tuple of:
    - out: Output data
    - cache: (x, act) ## I changed this
    """
    out = None
    ###########################################################################
    # TODO: Implement the max pooling forward pass                            #
    ###########################################################################
    
    # Unpack variables
    N, C, H, W = x.shape
    H_pool = pool_param['pool_height']
    W_pool = pool_param['pool_width']
    S = pool_param['stride']        
    Hout = (H - H_pool) / S + 1
    Wout = (W - W_pool) / S + 1
    
    # Hout and Wout are floats after /
    if all([int(Hout) == Hout, int(Wout) == Wout]):
        Hout = int(Hout)
        Wout = int(Wout)
    else:
        raise ValueError("Non-integer output size: {}x{}".format(Hout, Wout))

    out = np.zeros((N, C, Hout, Wout))
    # Keeping track of activation indexes, contains a (act_h, act_w) tuple for each coordinate of out
    act = np.zeros_like(out, dtype=np.ndarray)
    
    for n in range(N):
        img = x[n, ...]  # One image (C, H, W)
        for ho in range(Hout):
            for wo in range(Wout):
                # Img slice through all channels with space dims equal to (H_pool, W_pool)
                img_slice = img[:, ho*S : ho*S+H_pool, wo*S : wo*S+W_pool]  # (C, H_pool, W_pool)
                for c in range(C):
                    max_val = np.max(img_slice[c, ...])
                    max_idx = np.argmax(img_slice[c, ...])
                    
                    out[n, c, ho, wo] = max_val
                    
                    # Activation locations for backpropagation
                    act_h, act_w = np.array([ho*S, wo*S]) + np.unravel_index(max_idx, (H_pool, W_pool))
                    act[n, c, ho, wo] = np.array([act_h, act_w])
    
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, act) ## I changed this
    return out, cache


def max_pool_backward_naive(dout, cache):
    """
    A naive implementation of the backward pass for a max pooling layer.

    Inputs:
    - dout: Upstream derivatives
    - cache: A tuple of (x, act) where act is the activation map ## I changed this

    Returns:
    - dx: Gradient with respect to x
    """
    dx = None
    ###########################################################################
    # TODO: Implement the max pooling backward pass                           #
    ###########################################################################
    
    # Unpack variables
    x, act = cache
    N, C, _, _ = x.shape
    
    dx = np.zeros_like(x)
        
    # Route dout to the max values
    for n in range(N):
        for c in range(C):
            for (act_idx, dout_value) in zip(act[n, c, ...].flatten(), dout[n, c, ...].flatten()):
                act_h, act_w = act_idx
                dx[n, c, act_h, act_w] = dout_value
    
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx


def spatial_batchnorm_forward(x, gamma, beta, bn_param):
    """
    Computes the forward pass for spatial batch normalization.

    Inputs:
    - x: Input data of shape (N, C, H, W)
    - gamma: Scale parameter, of shape (C,)
    - beta: Shift parameter, of shape (C,)
    - bn_param: Dictionary with the following keys:
      - mode: 'train' or 'test'; required
      - eps: Constant for numeric stability
      - momentum: Constant for running mean / variance. momentum=0 means that
        old information is discarded completely at every time step, while
        momentum=1 means that new information is never incorporated. The
        default of momentum=0.9 should work well in most situations.
      - running_mean: Array of shape (D,) giving running mean of features
      - running_var Array of shape (D,) giving running variance of features

    Returns a tuple of:
    - out: Output data, of shape (N, C, H, W)
    - cache: Values needed for the backward pass
    """
    out, cache = None, None

    ###########################################################################
    # TODO: Implement the forward pass for spatial batch normalization.       #
    #                                                                         #
    # HINT: You can implement spatial batch normalization using the vanilla   #
    # version of batch normalization defined above. Your implementation should#
    # be very short; ours is less than five lines.                            #
    ###########################################################################
    
    N, C, H, W = x.shape
    
    # Convert dimensions of x: (N, C, H, W) -> (N, H, W, C) -> (N*H*W, C)
    x = x.transpose(0, 2, 3, 1).reshape(N * H * W, C)
    # Use vanilla batchnorm, forward pass
    y_batch, cache = batchnorm_forward(x, gamma, beta, bn_param)
    # Transpose result back to orig shape: (N*H*W, C) -> (N, H, W, C) -> (N, C, H, W)
    out = y_batch.reshape(N, H, W, C).transpose(0, 3, 1, 2)
    
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return out, cache


def spatial_batchnorm_backward(dout, cache):
    """
    Computes the backward pass for spatial batch normalization.

    Inputs:
    - dout: Upstream derivatives, of shape (N, C, H, W)
    - cache: Values from the forward pass

    Returns a tuple of:
    - dx: Gradient with respect to inputs, of shape (N, C, H, W)
    - dgamma: Gradient with respect to scale parameter, of shape (C,)
    - dbeta: Gradient with respect to shift parameter, of shape (C,)
    """
    dx, dgamma, dbeta = None, None, None

    ###########################################################################
    # TODO: Implement the backward pass for spatial batch normalization.      #
    #                                                                         #
    # HINT: You can implement spatial batch normalization using the vanilla   #
    # version of batch normalization defined above. Your implementation should#
    # be very short; ours is less than five lines.                            #
    ###########################################################################
    
    N, C, H, W = dout.shape
    
    # Convert dimensions of dout: (N, C, H, W) -> (N, H, W, C) -> (N*H*W, C)
    dout = dout.transpose(0, 2, 3, 1).reshape(N * H * W, C)
    # Use vanilla batchnorm, backward pass
    dx_batch, dgamma, dbeta = batchnorm_backward_alt(dout, cache)
    # Transpose result back to orig shape: (N*H*W, C) -> (N, H, W, C) -> (N, C, H, W)
    dx = dx_batch.reshape(N, H, W, C).transpose(0, 3, 1, 2)
    
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return dx, dgamma, dbeta


def svm_loss(x, y):
    """
    Computes the loss and gradient using for multiclass SVM classification.

    Inputs:
    - x: Input data, of shape (N, C) where x[i, j] is the score for the jth
      class for the ith input.
    - y: Vector of labels, of shape (N,) where y[i] is the label for x[i] and
      0 <= y[i] < C

    Returns a tuple of:
    - loss: Scalar giving the loss
    - dx: Gradient of the loss with respect to x
    """
    N = x.shape[0]
    correct_class_scores = x[np.arange(N), y]
    margins = np.maximum(0, x - correct_class_scores[:, np.newaxis] + 1.0)
    margins[np.arange(N), y] = 0
    loss = np.sum(margins) / N
    num_pos = np.sum(margins > 0, axis=1)
    dx = np.zeros_like(x)
    dx[margins > 0] = 1
    dx[np.arange(N), y] -= num_pos
    dx /= N
    return loss, dx


def softmax_loss(x, y):
    """
    Computes the loss and gradient for softmax classification.

    Inputs:
    - x: Input data, of shape (N, C) where x[i, j] is the score for the jth
      class for the ith input.
    - y: Vector of labels, of shape (N,) where y[i] is the label for x[i] and
      0 <= y[i] < C

    Returns a tuple of:
    - loss: Scalar giving the loss
    - dx: Gradient of the loss with respect to x
    """
    shifted_logits = x - np.max(x, axis=1, keepdims=True)
    Z = np.sum(np.exp(shifted_logits), axis=1, keepdims=True)
    log_probs = shifted_logits - np.log(Z)
    probs = np.exp(log_probs)
    N = x.shape[0]
    loss = -np.sum(log_probs[np.arange(N), y]) / N
    dx = probs.copy()
    dx[np.arange(N), y] -= 1
    dx /= N
    return loss, dx
