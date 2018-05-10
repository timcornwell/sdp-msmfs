for i in range(niter):

    # Lines 2 - 6
    mscale, mx, my, mval = find_global_optimum(hsmmpsf,
    	ihsmmpsf, smresidual, windowstack, findpeak)
    scale_counts[mscale] += 1
    scale_flux[mscale] += mval[0]

    # Line 7
    peak = numpy.max(numpy.fabs(mval))
    lhs, rhs = overlapIndices(ldirty[0, ...],  psf[0, ...], mx, my)

    # Lines 8 - 10
    m_model = update_moment_model(m_model, 
    	pscalestack, lhs, rhs, gain, mscale, mval)
    
    # Lines 11 - 15
    smresidual = update_scale_moment_residual(smresidual, 
        ssmmpsf, lhs, rhs, gain, mscale, mval)

    if peak < absolutethresh:
        break


