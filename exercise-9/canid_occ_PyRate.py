#!/usr/bin/env python
from numpy import * 


data_1=[array([15.777453,14.028906,14.112852,8.572445,15.828153,10.938903,15.498192,15.590086,15.956727,14.224086,14.728527,9.498296,11.764384]),
array([18.958459,17.009694,14.033949,14.156784,15.71033,14.936492,15.665244,15.076705,15.105487,14.760697,14.883379]),
array([15.512423,16.116259,14.161696,15.014332,12.728991,12.872331,14.156457,14.764603,14.045381,14.941738,6.259602,13.357865,14.254845,14.290325,14.708117,12.039644,7.899724,15.202183,15.202091,13.947942,13.096399,10.547781,14.374493,10.565665,15.586974,13.723834,12.938133,13.758357,16.991841,15.615061,14.931637,17.600912,13.803537,15.369678,15.542169,15.101212,22.301376,15.545693,12.112149,14.501105,14.509231,6.719807,14.620783,13.436939,10.186751,17.330098,15.634627,13.820578,19.093613,17.340754,14.287247]),
array([15.724481,14.469015,14.783469,14.36581,15.940974,14.028495,14.665805,15.413831,14.711805]),
array([14.378197]),
array([12.59253,14.998216,11.243648,10.834616,10.877237,12.303531,12.863576,21.296085,15.564578]),
array([13.062298,13.255674,12.428823,13.508917,15.05636,13.484156,6.003501,20.985927,10.315869,13.443713,10.526997,11.194364,11.948452,11.901083,12.560206,12.339381,13.578125,20.478733,6.455667,12.88728,9.471315,11.609638,12.94129,10.827395,13.464736,10.593161,11.007993,11.48175,10.57677,13.144156,11.087288,7.020221,11.406464,13.422826,11.344505,12.085287,10.460377,12.850175,8.026318,10.936189,12.877602,10.805115,9.313828,10.73266,9.630918,11.880402,12.230626,12.409097,12.460381,11.770339,13.449048,11.835806,11.420987,16.475133,12.109482,10.283376,11.782895,12.308534,11.503336,8.498801,12.345352,13.050941]),
array([16.698825]),
array([4.119624]),
array([0.545269,1.788293,0.079941,0.031044,0.034097,0.040328,0.006733,0.050164,0.005077,0.007649,0.009694]),
array([23.731739]),
array([31.332104,33.111245,28.177717,24.283776,21.514622,20.868206,21.493359,28.364354,22.434104,25.184624,22.242754,25.830973,27.958881,28.111061,29.978373,30.124356,26.809901,29.554689,28.071586,28.906742,28.242191,28.390017,28.70858,29.012239,30.664577,23.979149,26.636928]),
array([32.584939,32.409427,31.830424,31.755567,31.814754,32.176985,32.869403,26.699677,28.304141]),
array([22.518425,22.124601,23.728703,19.754719,17.30326,14.719049,14.083765,9.116441,12.723678,12.939102,15.154632,13.45563,14.639827,11.614675,14.723477,12.030885,10.768502,12.771209,12.976427,12.881086,8.012276,14.328954,15.356681,13.206759,18.499379,14.770878,8.788324,6.381171,14.303226,6.381469,9.806189,11.344376,10.787915,19.889056,16.332024,17.87666,5.910414,18.918831,17.174786,16.293981,18.194856,18.986199,19.644201,16.843065,6.954047,14.615621,15.49281,10.590567,10.424934,11.101175,12.222061,12.344854,10.9219,12.369876,13.643146,15.788459,14.218046,20.225455]),
array([9.333115,8.870285,10.072436,5.921102,9.789884,7.838372,6.625916,5.383288,4.112412,8.2122,7.889529,9.823078,10.296451,9.605797,7.617175,7.583863,9.255885,6.798416,9.385519,7.234158,5.527287,8.356157,3.595016,3.249189,4.092908,3.87678,2.95508,4.655006,3.677306,2.046048,2.118259,2.089207,4.936139]),
array([4.176549,3.872312,3.647432,3.607785,2.423625,2.981749,2.572748,4.801634,4.771929,3.130634,3.543818,3.408849,4.151629,2.177898,3.134412,4.736066,3.699132,2.387044,2.856988,4.429449,4.365965,3.54414,2.937565,2.476783,4.007228,4.604307,4.411542,4.357645]),
array([3.770241]),
array([8.547613,9.976195,9.516928,21.591419,17.95992,5.311204,21.063551,4.44642,6.452957,3.52282,4.441525,4.721506,3.321165,2.873135,4.354484,2.477331]),
array([13.48616,21.070893,10.520172,11.698142,12.182778,12.088795,17.937082,12.597771]),
array([5.347881,4.914347,4.42875]),
array([5.051417,5.070254,8.908032]),
array([5.145971,6.708396,11.308391,7.232136,8.785013,6.502597,7.115918,6.179903,19.376571,8.926017,5.587506,7.440659,13.505926,5.247494,6.819704,6.304312,11.764713,13.261528]),
array([5.803065,20.744933,6.217994,4.912952,9.727247,8.034172,5.020448,9.151379,8.979259,6.395724,10.261264,8.788916,22.522104,20.732463,7.938214,7.776478,10.382886,9.76015,11.157181,9.364198,11.067729,5.080506,9.195824,9.869481,6.986844,9.229698,7.102351,5.309178,8.653955]),
array([22.895356]),
array([34.429381,33.94688,35.814422,33.826112,30.872802,22.153692,24.984865,27.735594,21.775908,25.399711,27.234689,25.535617,24.862011,20.825531,22.580102,30.449655,24.203939,16.141917,19.575771,17.825743,11.012318,12.233172,12.425473,18.502542,9.030473,10.588185,10.678663,5.610967,15.328661,13.48636,13.878859,14.782723,5.720928,15.047228,6.729069,6.285315,14.780295,13.622372,15.466201,10.61197,15.322383,14.826215,18.621183,17.989433,14.730224,7.564147,18.568807,2.512515,0.457116,4.588545,2.909851,4.335382,1.806191,2.762827,2.582612,4.312103,2.943715,0.977614,1.572124,1.577889,0.515852,1.121963,0.630236,1.698491,3.607515,3.697129,7.205367,13.468307,2.606561,1.41524,0.483819,3.156539,3.111286,2.240565,1.362425,2.37614,2.385125,2.580556,1.834021,4.62059,0.360822,0.665096,8.734039,6.887269,20.376137,3.844832,21.156756,0.868338,0.363057,1.758968,3.839302,2.71109,24.700913,2.623808,4.899012,7.223787,4.189571,0.647398,18.524908,0.724421,10.234817,0.388937,2.219071,4.757419,0.119673,0.020528,0.120459,2.585666,0.110486,0.108151,0.060487,0.025428,0.066153,5.589522,0.667572,3.5667,0.106229,0.098706,0.084157,25.326612,23.182835,24.185204,22.914496,8.634982,1.834114]),
array([25.177837,7.53464,13.062996,11.686179,11.457264,11.632258,11.830058,9.108965,14.829908,4.941209,11.403333,13.012106,10.451502,9.742565,11.140917,13.857689,8.497625,12.310087,11.910674,12.478731,13.475009,11.405838,11.446146,13.183187,13.054795,3.313878,0.08517,0.020589,2.172964]),
array([6.557826,6.099005,8.99717,3.408638,3.783817,3.304381,3.746001,3.722127,1.850783,2.236765]),
array([6.060869,5.711367,7.673583,2.435663,2.140548,2.667671,3.870534,3.839921,3.008778,4.548509,1.146209,0.653171,0.332532,0.370785,0.770856,0.664868,1.702378,0.543554,0.165302,1.715615,0.541313,0.711941,0.758182,0.070928,3.165374,2.593301,2.688224,2.793455,2.539601,2.758059,3.552264,2.742941,2.998033,3.078852,3.520515,0.872208,0.009763,2.578384,2.099537,20.918397,4.374005,0.071355,0.004194,0.007169,0.004138,1.20031,0.009758,0.010234,0.008892,0.182087,0.629444,3.354771,1.204164,1.450066,0.005283,0.009182,0.009876,0.003106,1.73576,0.006669,0.484391,0.739677,0.008417,8.747781,5.225094,2.100098,1.645718,4.056108,4.965724,1.995825,2.338843,1.168954,0.866551,2.282655,0.930349,0.706729,0.442935,1.613112,4.018401,0.062726,0.396662,4.341278,4.64407,1.67451,2.122227,2.085399,2.445557,1.881597,0.12054,2.494537,2.494726,1.241004,1.274062,1.79448,1.075256,2.337971,1.965386,1.541027,1.735957,1.882473,1.555785,0.689479,3.167204,0.498633,0.663598,4.18122,0.819826,3.090179,2.651699,2.710936,2.614472,1.247588,2.514836,0.821699,1.741096,0.617383,0.376373,4.657629,4.819071,1.547204,2.038773,0.140522,2.479436,0.767447,2.399981,0.101924,0.144683,2.205423,3.368091,3.052283,5.075786,1.673169,2.100454,3.450052,4.731947,5.029975,3.979619,1.041978,1.219809,1.936837,1.405209,4.603021,0.268996,6.670938,3.496856,1.696688,1.997861,2.416731,1.995314,1.040855,1.477295,0.382645,1.732692,0.731051,0.561506,0.500811,0.252275,0.454953,1.490259,0.292655,0.188704,0.407056,1.22327,2.343469,2.14088,3.672008,2.635992,2.611469,1.93935,2.423377,2.469546,2.251357,1.637699,0.197514,0.138326,0.740307,0.381768,0.388888,0.596699,0.137628,0.39108,0.744345,0.998519,4.718976,1.940915,2.016906,1.435991,1.263227,2.581001,0.645061,1.605337,0.712651,4.498494,4.892019,3.425983,3.948714,3.647717,3.303405,3.102438,4.561048,4.212257,2.355969,2.263562,1.79882,4.263328,0.110587,0.084925,0.11034,2.516244,0.542259,0.018624,0.020041,0.009208,0.019666,1.241618,2.619081,3.95834,2.303402,1.738349,2.267051,0.019602,0.020266,0.090301,0.047237,0.12461,0.114014,0.422518,0.794627,9.927492,3.558948,0.002668,0.112305,0.212857,0.045172,6.921015,0.031714,0.006399,1.635783,0.677741,0.009434,0.009274,0.007188,0.011467,3.003129]),
array([0.178704,0.364465,0.558064,0.096131,0.117198,0.188353,1.073719]),
array([0.007131,0.008975,0.06924,0.047458,3.258338,0.352058,0.082656,0.373115,0]),
array([1.460222,0.666298,0]),
array([1.38752]),
array([4.232188,1.628391,0.511214,1.61799,0.901864,1.681778,1.500743,1.027215,0.602947,0.374064,1.53157,1.786998,1.263037,0.049714,0.898502,1.041098,1.966072,1.085155]),
array([0.009835,1.141576,1.240937,1.332303,1.974988,0.003343,0.654056,1.611046,0.723502,3.243109,2.290881,0.262216,0.29063,0.008906,0]),
array([0.674521]),
array([0.779854,0.603638,0.950554,1.727578,0.399968,0.654274,0.327806,0.584763,0.68003,0.277787,0.70881,0.029702,0.640825,0.724739,1.641756,0.050602,0.105006,0.074846,0.038292,0.038038,0.038047,0.045704,0.184037,0.080611,0.026019,0.123299,0.055564,0.084525,0.119471,0.055663,0.222037,1.466156,0.089048,0.097317,0.115348,0.019387,0.016452,1.275363,0.042564,0.041842,0.018599,0.039141,2.385503,0.083825,0.22152,0.143738,0.053646,0.012926,0.048106,0.118442,0.886187,0.043441,0.106089,0.076097,0.032572,0.084947,0.012367,0.108567,0.073781,0.058959,0.044561,0.032443,0.034129,0.058908,0.113606,0.076817,0.099581,0.067567,0.055447,1.725504,0.597244]),
array([2.64099,2.72472,1.496419,0.881374,1.775812,0.45754,2.529097,0.611596,1.659669,0.743475,1.2567,1.48679,2.626995,0.657231,0.87128,0.509654,1.580379,1.680248,3.422359,2.725613,2.167551,4.248308,1.483922,0.649468,1.622317,1.315034,1.729092,1.369768,0.711409,11.327545,3.19474]),
array([0.010858,0.882976,0.011069,0.004511,0.009838,0.001317,0.010026,0.004315,0.009542,0.108549,0.003118,0.00777,0.00382,0.010944,0.010848,0.009132,0]),
array([10.197439,8.292156,6.568829,9.999404,3.427534,1.958462,2.59337,2.368267,3.036687,4.490726,4.046019,2.977536,6.204245,10.292323,6.977879,5.781739,2.199969]),
array([0.618423,4.605084,4.47991,4.662505,2.06362,2.190599,2.457584,3.074042,3.384446,3.98961,1.621558,0.962329,0.575619,0.835557,1.133869,0.396661,1.04875,0.322843,1.555032,1.564839,0.942177,0.316594,0.910299,1.231046,1.229812,1.041144,0.528667,0.396272,1.311568,0.449729,0.624228,0.750308,0.819332,1.061493,0.561468,0.43455,1.250001,0.534815,0.070264,1.367467,1.07696,1.637286,1.771856,1.514016,1.562091,0.10133,0.078804,0.017862,0.012238,0.022319,0.014036,0.043232,0.04873,0.024542,0.015489,0.113285,0.044744,0.005895,0.120088,0.019543,0.003592,0.047673,0.114368,0.116064,0.011511,1.831639,0.121563,0.041189,0.055084,0.074549,0.106581,0.076072,0.062842,0.063549,0.09863,0.108366,0.008722,0.048728,0.051109,0.124323,0.082679,0.061169,0.290893,0.203947,0.028922,0.024316,0.043726,0.101542,0.0751,0.754789,1.100978,0.692476,0.503171,0.662765,0.009718,0]),
array([8.470279,4.843283,4.890264,2.283185,2.947287,4.232754,3.947089,4.216448,2.661711,3.11896,2.936075,3.419155,1.861132,3.456921,2.859664,3.06721,3.278295,2.515884,2.127162,3.410362,3.514499,2.960814,3.406026,4.076499,4.071179,3.335786,2.961597,3.654412,3.990658,1.960357,3.819543,2.636463,2.979686,1.975934,4.437987,0.0701]),
array([0.986378,1.613643,1.367885,1.796486,0.114124,0.063037,0.049144,0.073432,1.462013,0.966769,1.294162,2.184138,0.562353,0.600387,3.157063,1.263694,2.046103,0.641432,0.127322,2.240793,0.499157,0.635542,0.350425,1.608946,1.708556,2.073605,0.392017,0.3147,0.179872,0.289191,0.064193,0.072782,0.083611,0.098535,0.095693,1.73691,0.742709,0.736014,0.194916,0.732995,0.373643,1.026105,0.197516,0.016582,0.425895,0.77006,0.706475,1.639034,0.039469,0.212257,0.26755,0.473412,0.680962,0.373586,0.23517,0.29723,2.429144,0.28908,0.631514,0.742087,0.937569,0.745828,0.007973,0.011308,1.235028,0.389257,2.685384,0.078557,0.039984,0.088124,0.111846,0.120752,0.055887,0.116256,0.107844,0.078473,0.052666,0.088264,0.092881,0.089411,0.233753,0.061091,0.06736,0.064246,0.078736,0.100653,0.07324,0.114104,0.087054,0.258438,0.244321,0.012933,0.016764,0.118656,0.004654,0.006179,0.010584,1.608224,0.078944,0]),
array([1.222208,3.962513,3.469608,0.011375,0.006102,3.137852,1.757402,1.292451,2.917457,2.058583,1.367146,0.010098,1.330788,1.249786,0.007366,2.222148,1.935284,1.561587,0.096644,1.447451,0.616744,0.695409,1.519719,2.329843,2.354853,1.615756,1.173465,2.390709,1.595895,1.675588,3.66058,1.210119,1.195068,2.026078,1.640877,0.721862,0.183481,2.229235,1.382249,2.988081,1.567099,1.200359,0.008617,0.076368,0.029224,0.099968,1.878237,0.042725,0.015618,0.57312,2.263768,2.529144,0]),
array([1.362478]),
array([3.38145,3.586153,1.901758,1.261103,2.287298,1.786947,0.09474,0]),
array([3.152203]),
array([14.885572,16.221955,14.237572]),
array([13.818121,12.104978,14.476305,14.234035,14.67637,15.733588,15.065121,15.303031,14.214638,14.703349,15.74855,14.824386,13.752542,15.87272,21.794533,13.657812,14.302062]),
array([6.393434,5.568704,9.797825]),
array([11.782881,12.422565,10.469812,10.787921,11.631545,12.414326,11.083786,10.573792,12.581064,15.952658,10.85149,12.763948]),
array([12.265813,12.636109,12.439685,12.271842,12.265952,10.879061,10.420602,12.78847,6.81767,15.54363,14.749293]),
array([4.267337,4.176224]),
array([8.964997,4.493441]),
array([0.002542,0.049837,0.107564]),
array([46.814174]),
array([2.077178]),
array([2.134922,1.668326]),
array([4.318768,2.511526]),
array([28.178023]),
array([29.927767,27.559224,24.33216,24.606179,22.479664,15.81711,19.320962,28.814072,25.046207,25.956712]),
array([28.944205,21.615355,20.639038,22.02546,20.559003]),
array([2.087382]),
array([0.381258,0.177215,0.454923,0.493498,0.347521,0.757847,0.526854,0.683833,0.644728,0.500011,0.493516,0.044891,0.242544]),
array([2.442514,0.676557,0.089886]),
array([27.87593,23.491439,23.203094,20.608401,20.72587,22.662619,16.6105,19.858335,18.873917,18.344592,16.358315,15.999289,20.018734,19.230629,16.238056,19.864691,18.24347,17.375193,18.57428,18.519059,16.83743,17.162188,17.852519,19.406098,19.266566,16.18553,16.026154,19.482858,15.823383,17.441176,16.752586,19.804937,19.510841,18.761888,16.419296,16.987465,16.979441,16.77181,17.860758,16.978881,19.703185,20.404814,15.858049,15.19591,15.815017,15.894978,22.891314]),
array([17.002319,17.573039]),
array([16.687751,16.266174]),
array([21.146659]),
array([27.386427,30.026193,26.246925,28.236372,30.103702,21.402674]),
array([23.453586,22.440128,20.504893,22.283006]),
array([22.76157,26.5457,30.618456,29.076718,26.375494,28.274166,27.633524,29.098689,27.134149]),
array([16.272793,19.490613]),
array([11.668396,14.646146,10.33135]),
array([10.699107,10.809669,18.421746,11.657082,13.081471,12.714949,12.317131,13.455854,13.361873,12.506012,13.57979,11.781044,10.490663,10.356266,5.789772,8.256119]),
array([14.193877,13.890647,15.129254]),
array([14.839992,20.055837]),
array([14.068702,13.793677,13.732927,14.544052,13.666817,15.052388,15.609352]),
array([11.498364,11.644114,12.425117]),
array([14.375353]),
array([29.184013]),
array([32.348421,33.239747,31.047289,33.244967,32.471172,30.811201,32.934821,31.732564,28.29766,27.101259,23.212319,28.605361,24.638059,28.112515]),
array([28.537288,31.042427,30.632018,41.889811,36.931054,35.296892,34.050921,51.327994,28.846704]),
array([37.056923,34.20294,36.761921,36.702373,35.351008]),
array([1.702667,0.417248,0.099564,0.706671,0.111548,1.939317]),
array([0.045653,0.503481,0.745686,0.702233]),
array([22.354334]),
array([16.20176,17.054219,19.062029,16.552511,18.535697,20.252252,18.297013,17.649]),
array([22.550881,22.796674,22.670034,21.132837,20.718003,20.726676,20.870614,20.929684,23.071233,22.379735,23.337663,23.726178,23.840361,24.611966,20.677727,22.424815,21.045764,21.842124,24.741669,23.229285,23.927047,17.777919,17.656798,19.162503,16.205915,18.677646,19.14221,19.825496,20.419937,18.795531,26.389267,18.445684,17.811904]),
array([0.003916,0.006976,0.078938,2.220359,0.009487,0.002967,1.449538,0.044166]),
array([0.085733,0.58654,0.634918,0.035474,0.086114,0.017771,0.125053]),
array([0.903117]),
array([0.478344]),
array([32.548381,22.658222]),
array([23.049695]),
array([18.594296,19.136629,17.682359]),
array([32.778509,27.197427,24.36268,24.021217,30.399101,26.2162]),
array([23.812412]),
array([21.478558,24.332851,24.859005,26.787659,21.868204,24.231791,23.424398,23.785695]),
array([26.453722,21.485244,24.672618,25.449484,25.859056,29.395337,30.627919,26.21513,23.765391,25.71408]),
array([21.267721,22.173877]),
array([7.643496,8.959644,12.968084,7.381947,10.031798]),
array([7.228695]),
array([17.93333,5.152745,8.254186,6.798055,9.9232,6.671848,6.342582,11.529666,12.766058,12.339002,7.126218,7.422945,7.105712,12.150208,12.230429,13.161181,7.354564,12.776205,7.175274,10.629868,12.835493,13.497545,22.711962,6.236869,5.508503,10.723294,12.723053,11.303596,5.021397,7.864921,11.670385,7.129722,12.49942,13.377997,13.509799,10.058621,11.55817,8.303121,8.068261,21.627891,5.373314,8.292804,11.419853,6.196059,8.900613,6.207964,12.452312,17.040866,19.555907,13.005988,12.469864,12.12587,6.051485,8.104647,18.120711,11.727128,5.044523,12.858601,12.705819,5.698234,18.50675,19.4686,12.944843,12.924931,15.87002,6.754168,16.251574]),
array([13.354656,7.860122,10.100854,10.826841,10.531148,13.408147,12.787596,11.074129,9.46158,8.489427,11.134009,12.288874,11.747575,12.664492,11.148933,12.369191,10.438789,13.22545,10.846993,10.409199,12.114991,13.208347,13.280935,13.556642,12.027244,13.374365,11.924156,8.783719,7.166214,20.861093,10.207763,10.766254,11.294791,17.983495,12.796835,9.978699,12.029705,11.935232,12.081347,7.015381,12.402266,7.626902,12.650246,12.513044,20.497482,9.269033,14.286742,13.263379,12.709165,13.194038,11.156268,11.782467,12.761934,6.363923,5.495557,14.618844,13.947966,14.808254,14.495446,14.690034,14.880499,10.39079,7.285604,12.669015,9.699777,21.487544,11.087857,11.229512,7.450006,13.053969,11.118727,12.213751,10.311005,15.183781,5.194718,14.097225]),
array([6.722543,4.972889,7.259442]),
array([6.677327,9.974281,6.695532,6.28553,6.122811,5.057806,6.039145,10.05553,8.286365,15.315697,5.849715,6.30413,7.651567,7.5685,8.790665,5.393562,6.832604,4.036477,4.105865,10.151574,8.750297,6.689338,8.373362,8.046995,7.796124,8.340353,5.329514,10.203856]),
array([13.025392]),
array([14.149575,16.079986,18.897156,14.660353,14.869531,15.367184]),
array([16.294571]),
array([15.861711,13.194202]),
array([43.539009,36.002279,36.616347,36.667629,35.766622,34.959853,34.820297,34.935651,34.386216,35.1828,34.239268,35.597908,35.474289,34.922716,36.603836,36.193777,34.311424,33.35345,33.348002,33.330498,33.836376,33.721832,33.511752,33.771499,33.426228,33.392958,33.787903,29.138415,32.341845,31.602553,32.625127,31.362851,31.184577,20.967865]),
array([33.746616,33.552409]),
array([38.076209,33.948838,36.227258,35.92231,36.528264,36.337952,35.902431,35.472914,37.085387,35.332953,36.613284,35.7556,35.405292,34.651102,35.874511,35.827775,34.309324,35.89413,36.429907,34.359553,35.445467,35.479983,34.149312,35.741065,34.294162,36.723457,35.74978,35.386119,34.827145,36.717859,34.319221,36.939915,34.751769,36.953722,36.754175,35.718423,36.727073,36.143361,33.708921,33.45282,33.536546,33.848031,33.348305,33.824753,33.562901,33.684907,33.451694,33.771373,33.42451,33.563895,33.547789,33.513203,33.582023,33.532335,33.55459,33.875407,33.617696,33.726162,33.883666,33.671714,33.863362,33.738556,33.725578,33.434834,33.865631,33.405794,33.409657,33.620669,33.313662,33.394075,33.38467,33.678427,33.408281,33.873076,33.546423,33.609054,33.649347,33.691327,33.6597,33.346395,33.487759,33.462397,33.5969,33.633852,33.733321,33.522677,33.499145,33.573328,33.867493,33.679759,33.677048,33.544781,33.436055,33.605329,33.793523,33.743474,33.380259,33.342544,33.385095,33.659511,33.767823,33.597865,33.53965,33.662806,33.511113,33.551125,33.554585,33.612086,33.790468,33.838533,33.894856,33.557286,33.893634,33.614726,33.47278,33.400012,33.633942,33.442558,33.493218,33.566332,33.496768,33.562798,33.431807,32.801308,30.988409,31.487286,32.743677,31.92285,31.997775,31.834133,35.824157,35.301458,33.707092]),
array([28.916207,21.646191]),
array([24.329599,20.721617,13.858483,13.823442,13.861418,13.542691,12.194209,12.30386,14.412392,11.513924,17.436534,28.343503,14.764079]),
array([28.330801]),
array([26.377856,26.870372,27.995503,26.656399,26.615671]),
array([21.784398,24.641361,22.917789,23.919214,21.843438,23.548474]),
array([13.829724,18.855278,16.948006,18.338466,16.33542,24.551587,18.910235,19.38586,16.927528,19.904388,18.159245,17.465694,19.201701,18.291405,14.883389,14.212138,15.547788,13.879038,15.803177,13.696416,15.707971,14.294188,15.909107,15.814807]),
array([13.322506,12.068417,13.065868,10.401585,11.850379,11.29271,11.247686,10.703108,13.165426,9.57788,10.371134,13.403458,12.612362,11.488105,11.234994,13.064251,13.137705,13.444973]),
array([24.712537]),
array([11.643539]),
array([15.738889,14.976744,13.835694,10.509988,14.159619,15.501084,12.869208,14.784653,13.811234,13.74993,14.307928,15.030248,13.698894,15.855774,13.727918,14.55907,15.129649,12.761695,15.635737,15.655301,13.947788,12.645793,15.180402,11.344571,13.217241,14.620098,12.376557,13.026276,13.50995,15.606668,13.868061,15.296097,15.832096,15.854784,15.187122,13.080485,12.826614,10.37947,12.91732,11.320447,12.344869,12.819516,15.189191,18.688017,16.537199,5.968818,11.057777,12.925661,20.854038,15.842197,11.803197]),
array([20.758531,20.308517,22.098671,19.51391,18.954235,24.631418]),
array([1.687513,0.227013,1.828694,4.377115,0.075908,0.567977,3.480998]),
array([0.008603,1.257843,1.559536,0.132717,0.581766,1.326934,0.805615,2.323432,1.798125,0.039316]),
array([25.308763]),
array([26.529405,22.417494,27.164294,26.469788,26.168052]),
array([23.923921,30.669904]),
array([33.485316,32.069948,30.809733,31.6329,32.699287,31.380432,32.772076,31.916846,31.119728,32.401059,32.469535,32.850828,32.655828,31.72629,30.243819,26.821381,29.05886,30.747837,28.449345,27.629277,21.561672]),
array([5.572045]),
array([12.379126,17.779758,18.609855]),
array([6.716376,5.612089,5.372977,6.991022,13.043762,12.920597]),
array([10.76627]),
array([18.657421,16.060248,16.351966,16.498755,17.615959,18.074485,17.947103,19.328661,17.73338,18.795084,16.292239,18.731956,20.300761,16.485147,18.865205,17.885715,16.993084,18.690003,17.163089,17.72298,19.578816,16.054709,19.603568,18.821295,17.781714]),
array([17.418089,15.00659,19.916301,17.060156,19.029936,17.113757,17.597797,17.391101,13.690085,18.363619,22.78771,16.418292,15.89406,22.039316,13.637408,12.580012,14.194768,15.356504,13.726988,18.968006,14.187837,14.607533,13.752915,15.351065,15.592122,14.374195,16.369672,15.258185,15.174058,13.691964,14.584563,14.583372,15.208181,15.43926]),
array([45.099443]),
array([5.231224,3.888137,5.073605,3.34463,1.66367,3.09215,2.656771,0.238134,2.656004,2.755039,3.263008,2.741484,0.801015,5.312022,4.423776,3.979633,2.571822,2.946873,8.179925,3.878188,3.314425,3.740352,1.431187,2.794518,1.941595,2.038717,1.89044,1.960023,2.956825,2.252766,2.807033,1.101469,2.201309,4.67477,3.994027,4.72998,0.888766,1.064812]),
array([2.688513,2.995896]),
array([1.663842,0.091936,0.02429]),
array([23.144671,18.351223]),
array([14.702335,18.50263,20.194914,16.738409,18.206371,19.86908,16.620445,19.503136,16.484282,13.994045,14.468376,14.414079,13.743832,14.341524]),
array([16.707183,18.834315,17.289344,17.423336]),
array([33.844747,31.627011]),
array([18.074568,20.24399,18.16789]),
array([32.744153,31.88498,22.346404]),
array([26.403865]),
array([25.679262,29.205304,22.319277,25.693856,29.42973,29.517026]),
array([33.393899,33.771216]),
array([0.81608,0.339173,2.627359,1.613076,1.309086]),
array([0.004003,0.006177,0.544261,0.127689,2.092281,1.660486,0.112297]),
array([30.95892,30.925437]),
array([33.219337,32.169028,32.948141,33.242614]),
array([16.909193,20.425837,9.30305,18.093009,17.782383,14.765324,18.679525,16.190751,17.225301,19.415967,14.817906,14.612113,22.405751,16.841653,15.703724,19.166766,14.731114,15.256083]),
array([19.506969,17.252412,19.317422,14.198316,18.470859]),
array([26.459722,25.376473,28.556953,30.008476,26.295713,24.181611,26.789404,21.419709,23.668018,24.139217,21.213554,26.269301]),
array([20.437481,23.820183]),
array([20.822981,22.123772,22.241165,23.639979,22.333852,23.919512,29.692282,27.845737]),
array([12.102156,12.100094,10.907642,8.756638,12.011837,9.176948,11.739339,12.231344,13.553108,12.498287,13.172817,11.581259,12.461716,12.496862,12.030837,11.302062,12.729794,16.837928,13.122821,13.031044,13.469781,11.088953,12.871591,10.901723,11.633396,12.084026]),
array([15.234004,14.370064,13.860268,14.119678,15.217826,14.003001,14.590009,14.236857,15.692539,14.037091,15.867637,13.894582,13.659811,14.899481,15.2616,7.538326,14.930556,15.177581,21.830288,14.318669,14.339286,15.809519,14.046978,15.534757,15.405856,17.116117,14.10322,14.811346,13.849813,14.637875,14.576525,14.540551,16.802776,15.892266,15.557553,16.652915,10.764817,15.280337,13.669193,14.094846,15.670829,15.314594,15.525065,15.848937]),
array([24.009355,27.619119,26.702132,26.874696,30.2867,27.437295,27.914251,20.735997]),
array([24.500902,23.524484,16.134473,17.737012,20.504356,18.767286,18.854071,17.180391,27.142787]),
array([24.651184]),
array([24.762033,20.704485,20.827837,22.049425,23.807529,22.221025,22.004454,23.818389]),
array([30.899452,24.396243,25.335838]),
array([23.518096,24.697539,17.255255,19.213095,17.90523,17.49279,19.62501,17.336517,20.302796]),
array([18.786689]),
array([20.148435,16.195538,17.518071,18.8098,16.621135]),
array([23.522265,25.674675,22.150613,21.361922,21.050531,20.615961,20.842101,22.153996,22.802343,23.064973,22.203161,19.959991]),
array([22.59925]),
array([30.752761,29.570708,24.277168,23.235553]),
array([19.0047]),
array([33.317403]),
array([15.35821,13.864735,13.792832,14.938968,13.738738]),
array([0.517601,0.635119,0.638747,0.161185,0.811682,0.08422,0.104766]),
array([0.513047]),
array([1.843202]),
array([0.424262,0.03585,0.114216,0.07825,1.280229,0.276267,0.122419,0.084078]),
array([18.526951,16.351996,16.42854,18.98227,19.605854,19.144651,20.354146,18.734638,19.138897,18.320837,19.443942,19.851102,17.404528,20.385418,16.34341,17.318114,17.280486,16.977406,16.336618,16.535706,15.024353,18.791813,16.495253,18.101567,14.492785,15.547905,6.935959]),
array([15.88448,16.859896,19.290369,15.209797]),
array([0.010029,2.159467,0.535942,0.455178,0]),
array([22.97842,25.30293,27.864325]),
array([0.728744]),
array([0.010061]),
array([22.17183,21.655522,30.223406,30.276015,27.583533]),
array([14.183529,14.128332,19.103681]),
array([0.033764,1.922759,0.697051]),
array([3.573505,2.329925]),
array([15.19059,15.422868,17.676422,14.288669,10.598565]),
array([17.860431,17.912452,18.165696,19.464115,14.306054,18.461628,16.599896,18.680427,18.566191,17.160662,17.118511,14.917299,15.148512,16.833935,13.300895,15.050705,14.300896,18.864997,19.351968,15.964084]),
array([18.861994,18.010425,16.44731,13.950263,18.888505,16.795558,19.546015,16.007559,19.239506,17.71264,19.030046,13.86345,16.64441,19.434718,20.197259,17.889991,14.297056,15.04684,14.593687,15.653021,14.951259,13.658799,14.397427,15.751018,13.926189,15.258246,13.860444,13.621698,13.680769,14.545386,15.097279,15.532826,15.526959,12.694914,13.68286]),
array([2.501437,0.126822,0.529251,1.657585,0.09497,0.105386,0.04204,0.075958,0.17512,13.043244]),
array([2.588994,0.832879,0.402619,0.768319,0.883076,1.528565,1.344277,0.088865,0.850306,0.061617,0.020343,0.117631,0.065569,0.047365,1.052664,0.108724,0.692211,0.072344,0.014558,0.107812,0.050374,0.104148,0.121454,0.040101,2.308853,0.076496,0.00849,0.119435,0.092715,0.080611,0.099861,0.058806,0.097797,0.074537]),
array([2.475734]),
array([4.86077,2.098402,3.499896,1.874213,4.334715]),
array([0.660177,0.484866]),
array([3.740509]),
array([9.878974]),
array([6.546708,5.927413,8.237302,8.814515,3.911661,1.697482,1.403579,0.92047,0.363003,0.662179,1.133049,1.761152,1.550394,0.829732,0.029804,2.120225,4.923129,4.519776,2.156002,1.526857,2.20753,2.75864,1.194705,4.56104,3.224054,4.926597,3.35665,1.186065,2.540331,2.031855,0.306334,0.628992,4.303177,1.988238,2.985249,3.167191,1.002871,2.367297,2.277261,2.014042,2.538306,4.594102,3.205469,0.102619,1.039689,1.358444,2.858152,0.936398,2.762255,2.882991,2.938628,3.116053,2.642392,4.473428,2.549896,2.29078,0.838767,1.913088,0.655734,0.631487,1.945638,1.888187,0.024065,0.085543,1.176511,2.810336,0.112535,0.764254,2.226163,1.369652,1.984428,2.072092,3.42858,8.478102,4.522854,2.415843,2.496647,0.276843,3.784189,0.112627,0.077449,0.034911,0.414047,0.132299,2.162705,0.27609,0.722165,1.654482,3.961312,2.621423,2.119101,1.158493,0.322143,0.593257,0.665283,2.403973,0.747485,4.176604,3.700407,0.537403,1.632414,0.036069,0.07738,0.013288,2.772605,1.657459,3.510354,0.079343,0.052016,0.120763,2.568156,4.29233,1.220433,1.246533,0.062826,0.00619]),
array([0.020586]),
array([0.007294,0.890067,0.004819,1.561338,0.004226,0.005307,0.004673,0.212856,0.007873,0.00445,0.008918,0.411336,2.197035,0.890792,0.918571,2.480106,0.049839,0.685791,1.843982,2.543236]),
array([10.60164]),
array([4.554425]),
array([5.152333,7.9877,5.298421,9.248126,12.252678,6.003332,8.770897,9.568615,8.123568,9.266405,8.164423,0.893496,8.38495,7.803108,8.880675,7.213984,6.523665,5.778169,10.24643,6.245247,14.493632]),
array([2.042459,1.10999,1.029651,1.189294,1.057597,1.081775,1.763125,1.286108,1.263292,0.116748,0.023048,0.060385,0.105692,0.019222,0.101446]),
array([1.21383,1.466335,0.952189,1.137111,0.098011,0.073932,0.093824,1.718962,1.618185,1.577621,0.075437,0.35492,0.141894,0.344398,0.03334,0.33209,1.483678,0.321215,0.326973,3.103145,1.308773,0.100624,0.408042,0.708172,0.116251,0.438011,1.059362,0.494648,0.102401,0.15632,0.595389,0.589438,0.874829,1.498912,1.018309,0.111829,1.115923,0.217931,0.713709,0.268721,2.26812,0.421973,0.046649,0.035029,1.637193,0.048487,0.083851,0.117322,0.106638,0.08613,0.118504,0.098743,0.061209,0.112246,0.012123,0.051289,0.040409,0.105934,0.025294,2.106377,0.063035,0.009806,0.00473,0.002897,0.095462,1.053491,0.043856]),
array([0.091086]),
array([0.070972]),
array([0.587094,2.504323,1.555588]),
array([0.85511,1.262034,0.249261,1.577086,0.169193,1.567637,0.627099,2.053755,0.162225]),
array([1.422501])
]

d=[data_1]
names=[ 'canid_occ_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Aelurodon','Aelurodon_asthenostylus','Aelurodon_ferox','Aelurodon_mcgrewi','Aelurodon_montanensis','Aelurodon_stirtoni','Aelurodon_taxoides','Aelurodon_wheelerianus','Alopex','Alopex_lagopus','Archaeocyon_falkenbachi','Archaeocyon_leptodus','Archaeocyon_pavidus','Borophaginae','Borophagus','Borophagus_diversidens','Borophagus_dudleyi','Borophagus_hilli','Borophagus_littoralis','Borophagus_orc','Borophagus_parvus','Borophagus_pugnator','Borophagus_secundus','Caedocyon_tedfordi','Canidae','Caninae','Canini','Canis','Canis_(Pseudalopex)','Canis_adustus','Canis_anthus','Canis_apolloniensis','Canis_armbrusteri','Canis_aureus','Canis_cedazoensis','Canis_dirus','Canis_edwardii','Canis_familiaris','Canis_ferox','Canis_latrans','Canis_lepophagus','Canis_lupus','Canis_mesomelas','Canis_proplatensis','Canis_rufus','Canis_thooides','Carpocyon','Carpocyon_compressus','Carpocyon_limosus','Carpocyon_robustus','Carpocyon_webbi','Cerdocyon_avius','Cerdocyon_texanus','Cerdocyon_thous','Chailicyon_crassidens','Chrysocyon','Chrysocyon_brachyurus','Chrysocyon_nearcticus','Cormocyon','Cormocyon_copei','Cormocyon_haydeni','Cubacyon_transversidens','Cuon','Cuon_alpinus','Cynarctoides_acridens','Cynarctoides_emryi','Cynarctoides_gawnae','Cynarctoides_harlowi','Cynarctoides_lemur','Cynarctoides_luskensis','Cynarctoides_roii','Cynarctoides_whistleri','Cynarctus','Cynarctus_crucidens','Cynarctus_galushai','Cynarctus_marylandica','Cynarctus_saxatilis','Cynarctus_voorhiesi','Cynarctus_wangi','Cynodesmus_martini','Cynodesmus_thooides','Cynodictis','Cynodictis_lacustris','Cynotherium','Cynotherium_sardous','Desmocyon','Desmocyon_matthewi','Desmocyon_thomsoni','Dusicyon','Dusicyon_avus','Dusicyon_culpaeus','Dusicyon_sechurae','Ectopocynus_antiquus','Ectopocynus_intermedius','Ectopocynus_simplicidens','Enhydrocyon','Enhydrocyon_basilatus','Enhydrocyon_crassidens','Enhydrocyon_pahinsintewakpa','Enhydrocyon_stenocephalus','Epicyon','Epicyon_aelurodontoides','Epicyon_haydeni','Epicyon_saevus','Eucyon','Eucyon_davisi','Eucyon_skinneri','Euoplocyon_brachygnathus','Euoplocyon_spissidens','Gobicyon','Hesperocyon','Hesperocyon_coloradensis','Hesperocyon_gregarius','Hesperocyoninae','Leptocyon','Leptocyon_delicatus','Leptocyon_douglassi','Leptocyon_gregorii','Leptocyon_leidyi','Leptocyon_matthewi','Leptocyon_mollis','Leptocyon_tejonensis','Leptocyon_vafer','Leptocyon_vulpinus','Lycaon','Lycaon_pictus','Mesocyon','Mesocyon_brachyops','Mesocyon_coryphaeus','Mesocyon_temnodon','Metalopex_bakeri','Metalopex_macconnelli','Metalopex_merriami','Metatomarctus','Metatomarctus_canavus','Microtomarctus_conferta','Neovulpavus_washakius','Nyctereutes','Nyctereutes_abdeslami','Nyctereutes_procyonoides','Osbornodon_brachypus','Osbornodon_fricki','Osbornodon_iamonensis','Osbornodon_renjiei','Osbornodon_scitulus','Osbornodon_sesnoni','Osbornodon_wangi','Otarocyon_cooki','Otarocyon_macdonaldi','Otocyon','Otocyon_megalotis','Oxetocyon','Oxetocyon_cuspidatus','Paracynarctus_kelloggi','Paracynarctus_sinclairi','Paraenhydrocyon_josephi','Paraenhydrocyon_robustus','Paraenhydrocyon_wallovianus','Paratomarctus_euthos','Paratomarctus_temerarius','Philotrox_condoni','Phlaocyon','Phlaocyon_achoros','Phlaocyon_annectens','Phlaocyon_latidens','Phlaocyon_leucosteus','Phlaocyon_mariae','Phlaocyon_marslandensis','Phlaocyon_minor','Phlaocyon_multicuspus','Phlaocyon_taylori','Phlaocyon_yatkolai','Protemnocyon_inflatus','Protepicyon_raki','Protocyon','Protocyon_orcesi','Protocyon_tarijensis','Protocyon_troglodytes','Protomarctus_optatus','Psalidocyon_marianae','Pseudalopex_gymnocercus','Rhizocyon_oregonensis','Speothos','Speothos_venaticus','Sunkahetanka_geringensis','Tephrocyon_rurestris','Theriodictis','Theriodictis_floridanus','Tomarctus','Tomarctus_brevirostris','Tomarctus_hippophaga','Urocyon','Urocyon_cinereoargenteus','Urocyon_citrinus','Urocyon_galushai','Urocyon_minicephalus','Urocyon_progressus','Urocyon_webbi','Vulpes','Vulpes_cascadensis','Vulpes_chama','Vulpes_kernensis','Vulpes_mathisoni','Vulpes_stenognathus','Vulpes_velox','Vulpes_vulpes','Vulpes_vulpes_macroura','Vulpini','Xenocyon','Xenocyon_lycaonoides','Xenocyon_texanus']
def get_taxa_names(): return taxa_names