from convert import quantize_q8_0, quantize_q4_0
import torch

# generated by:
#   torch.manual_seed(0)
#   weight = torch.randn(2, 128)
weight = torch.tensor(
        [[-1.1258e+00, -1.1524e+00, -2.5058e-01, -4.3388e-01,  8.4871e-01,
          6.9201e-01, -3.1601e-01, -2.1152e+00,  3.2227e-01, -1.2633e+00,
          3.4998e-01,  3.0813e-01,  1.1984e-01,  1.2377e+00,  1.1168e+00,
         -2.4728e-01, -1.3527e+00, -1.6959e+00,  5.6665e-01,  7.9351e-01,
          5.9884e-01, -1.5551e+00, -3.4136e-01,  1.8530e+00,  7.5019e-01,
         -5.8550e-01, -1.7340e-01,  1.8348e-01,  1.3894e+00,  1.5863e+00,
          9.4630e-01, -8.4368e-01, -6.1358e-01,  3.1593e-02, -4.9268e-01,
          2.4841e-01,  4.3970e-01,  1.1241e-01,  6.4079e-01,  4.4116e-01,
         -1.0231e-01,  7.9244e-01, -2.8967e-01,  5.2507e-02,  5.2286e-01,
          2.3022e+00, -1.4689e+00, -1.5867e+00, -6.7309e-01,  8.7283e-01,
          1.0554e+00,  1.7784e-01, -2.3034e-01, -3.9175e-01,  5.4329e-01,
         -3.9516e-01, -4.4622e-01,  7.4402e-01,  1.5210e+00,  3.4105e+00,
         -1.5312e+00, -1.2341e+00,  1.8197e+00, -5.5153e-01, -5.6925e-01,
          9.1997e-01,  1.1108e+00,  1.2899e+00, -1.4782e+00,  2.5672e+00,
         -4.7312e-01,  3.3555e-01, -1.6293e+00, -5.4974e-01, -4.7983e-01,
         -4.9968e-01, -1.0670e+00,  1.1149e+00, -1.4067e-01,  8.0575e-01,
         -9.3348e-02,  6.8705e-01, -8.3832e-01,  8.9182e-04,  8.4189e-01,
         -4.0003e-01,  1.0395e+00,  3.5815e-01, -2.4600e-01,  2.3025e+00,
         -1.8817e+00, -4.9727e-02, -1.0450e+00, -9.5650e-01,  3.3532e-02,
          7.1009e-01,  1.6459e+00, -1.3602e+00,  3.4457e-01,  5.1987e-01,
         -2.6133e+00, -1.6965e+00, -2.2824e-01,  2.7995e-01,  2.4693e-01,
          7.6887e-02,  3.3801e-01,  4.5440e-01,  4.5694e-01, -8.6537e-01,
          7.8131e-01, -9.2679e-01, -2.1883e-01, -2.4351e+00, -7.2915e-02,
         -3.3986e-02,  9.6252e-01,  3.4917e-01, -9.2146e-01, -5.6195e-02,
         -6.2270e-01, -4.6372e-01,  1.9218e+00, -4.0255e-01,  1.2390e-01,
          1.1648e+00,  9.2337e-01,  1.3873e+00],
        [-8.8338e-01, -4.1891e-01, -8.0483e-01,  5.6561e-01,  6.1036e-01,
          4.6688e-01,  1.9507e+00, -1.0631e+00, -7.7326e-02,  1.1640e-01,
         -5.9399e-01, -1.2439e+00, -1.0209e-01, -1.0335e+00, -3.1264e-01,
          2.4579e-01, -2.5964e-01,  1.1834e-01,  2.4396e-01,  1.1646e+00,
          2.8858e-01,  3.8660e-01, -2.0106e-01, -1.1793e-01,  1.9220e-01,
         -7.7216e-01, -1.9003e+00,  1.3068e-01, -7.0429e-01,  3.1472e-01,
          1.5739e-01,  3.8536e-01,  9.6715e-01, -9.9108e-01,  3.0161e-01,
         -1.0732e-01,  9.9846e-01, -4.9871e-01,  7.6111e-01,  6.1830e-01,
          3.1405e-01,  2.1333e-01, -1.2005e-01,  3.6046e-01, -3.1403e-01,
         -1.0787e+00,  2.4081e-01, -1.3962e+00, -6.6144e-02, -3.5836e-01,
         -1.5616e+00, -3.5464e-01,  1.0811e+00,  1.3148e-01,  1.5735e+00,
          7.8143e-01, -1.0787e+00, -7.2091e-01,  1.4708e+00,  2.7564e-01,
          6.6678e-01, -9.9439e-01, -1.1894e+00, -1.1959e+00, -5.5963e-01,
          5.3347e-01,  4.0689e-01,  3.9459e-01,  1.7151e-01,  8.7604e-01,
         -2.8709e-01,  1.0216e+00, -7.4395e-02, -1.0922e+00,  3.9203e-01,
          5.9453e-01,  6.6227e-01, -1.2063e+00,  6.0744e-01, -5.4716e-01,
          1.1711e+00,  9.7496e-02,  9.6337e-01,  8.4032e-01, -1.2537e+00,
          9.8684e-01, -4.9466e-01, -1.2830e+00,  9.5522e-01,  1.2836e+00,
         -6.6586e-01,  5.6513e-01,  2.8770e-01, -3.3375e-02, -1.0619e+00,
         -1.1443e-01, -3.4334e-01,  1.5713e+00,  1.9161e-01,  3.7994e-01,
         -1.4476e-01,  6.3762e-01, -2.8129e-01, -1.3299e+00, -1.4201e-01,
         -5.3415e-01, -5.2338e-01,  8.6150e-01, -8.8696e-01,  8.3877e-01,
          1.1529e+00, -1.7611e+00, -1.4777e+00, -1.7557e+00,  7.6166e-02,
         -1.0786e+00,  1.4403e+00, -1.1059e-01,  5.7686e-01, -1.6917e-01,
         -6.4025e-02,  1.0384e+00,  9.0682e-01, -4.7551e-01, -8.7074e-01,
          1.4474e-01,  1.9029e+00,  3.9040e-01]]
)

def test_quantize_q8_0():
    q8_tensor = quantize_q8_0(weight).int()
    ggml_q8_tensor = torch.tensor([68, 36, -68, -69, -15, -26, 51, 42, -19, -127, 19, -76, 21, 19, 7, 74, 67, -15, -81, -102, 34, 48, 36, -93, -20, 111, 45, -35, -10, 11, 83, 95, 57, -51, -32, 38, -23, 1, -18, 9, 16, 4, 24, 16, -4, 30, -11, 2, 19, 86, -55, -59, -25, 33, 39, 7, -9, -15, 20, -15, -17, 28, 57, 127, -57, -46, 68, -21, 45, 37, -28, 46, 55, 64, -73, 127, -23, 17, -81, -27, -24, -25, -53, 55, -7, 40, -5, 34, -41, 0, 42, -20, 51, 18, -12, 114, -93, -2, -52, -47, 2, 35, 69, 37, 80, -66, 17, 25, -127, -82, -11, 14, 12, 4, 16, 22, 22, -42, 38, -45, -11, -118, -4, -2, 47, 17, -45, -3, -30, -23, 93, -20, 6, 57, 45, 67, -35, 35, -58, -27, -52, 37, 40, 30, 127, -69, -5, 8, -39, -81, -7, -67, -20, 16, -17, 8, 16, 76, 19, 25, -13, -8, 13, -50, -124, 9, -46, 20, 10, 25, 88, 34, 78, -80, 24, -9, 81, -40, 61, 50, 25, 17, -10, 29, -25, -87, 19, -113, -5, -29, -126, -29, 87, 11, 127, 63, -87, -58, 119, 22, 54, -80, -96, -97, 45, 33, -55, 53, 40, 39, 17, 87, -28, 101, -7, -108, 39, 59, 66, -119, 60, -54, 116, 10, 95, 83, -124, 98, -49, -127, 95, 127, -66, 56, 28, -3, -105, -11, -84, 35, -23, 105, 13, 25, -10, 43, -19, -89, -9, -36, -35, 57, -59, 56, 77, -118, -99, -117, 5, -72, 96, -7, 38, -11, -4, 69, 61, -32, -58, 10, 127, 26]).view(q8_tensor.shape)
    assert (q8_tensor == ggml_q8_tensor).all()


def test_quantize_q4_0():
    q4_tensor = quantize_q4_0(weight).int()
    ggml_q4_tensor = torch.tensor([59, 52, 52, 36, -89, -74, -85, 43, 119, -16, -71, 99, 121, -103, -40, -19, -52, 87, -46, -74, -87, 104, 105, -121, -105, -104, 118, -105, -104, 102, 73, 8, -57, -77, 75, -100, 34, -75, -118, 101, -75, -124, 93, -112, 89, 119, -99, 26, -23, -118, -69, -75, -120, 101, 58, 53, 125, 20, -119, -118, -80, -109, 87, -119, 105, 120, -23, 121, -119, -59, -70, -59, -50, -77, -100, -118, 123, 54, 117, 102, -112, -116, 120, -72, -6, 125, -72, 124, 121, 103, 75, -78, -125, -83, -10, -87, 51, 123, 4, 69, -42, -57, 25, 118, 90, -35, -25, -17, 34, -79, 27, 117, 37, 54, -9, 35, -70, -14, 40, 15, -58, 68, 100, -113, -12, -101, -99, -77, -23, -15, -121, -42, 41, -123, 105, -98, -119, 74, 74, -92, -52, 116, 3, 111]).view(q4_tensor.shape)
    assert (q4_tensor == ggml_q4_tensor).all()
