<!--
 .. title: What are the calcite recrystallization rates in deep sea sediments
 .. slug: SrRate
 .. date: 2015-03-24 21:44:25 UTC-05:00
 .. tags: Carbonate diagenesis, Ocean Drilling Projects
 .. link: 
 .. description: 
 .. type: text
 -->


Methods
-------
In ocean drilling sites where calcite dissolution rate and precipitation rate are almost equal ($R_p=R_d$), the recrystallization rate $R$ can be defined as $R=R_p=R_d$. In such cases, Ca concentration cannot be used to calculate the recrystallization rates since the Ca concentration is affected only by the net precipitation rate, which is close to zero in these cases. Trace elements or isotopes, however, are not in equilibrium between the pore fluid and the solid. Their concentrations can therefore provide information on the exchange rate of calcite dissolution and precipitation. We use Sr concentration to infer the recrystallization which has been proven successful in Fantl and DePaolo (2007). 

The evolution of Sr concentration in the pore fluid ($C_f$) can be describe by the equation:
$$
\dfrac{\partial C_f}{\partial t}=D \dfrac{\partial ^2 C_f}{\partial z^2}-v\dfrac{\partial C_f}{\partial z}+f_cRM(C_s-KC_f),
$$
where $M=\rho_s (1-\phi)/(\rho_f \phi)$, $K$ is the equilibrium distribution coefficient of Sr between the solid and the fluid, and $f_c$ is the fraction of calcite in the solid. $z=0$ is defined as the interface between sea water and the sediment, and $z$ is positive in the downward direction. 

We assume that porosity, fluid density, solid density, the distribution coefficient $K$, Sr concentration in the solid $C_s$, and the recrystallization rate $R$ are all constants with depth. The value of M is close to 1.1 assuming that $\phi=0.7$. $K$ is close to 20, and $D$ is close to 7500 $m^2/Myr$ [@fantle2007isotopes].

We further assume that the Sr concentration is at steady state, so the term $\partial C_f/\partial t$ is zero. The Sr concentration in pore fluid at the upper boundary is fixed at the modern seawater concentration (91 $\mu M$). Under these conditions, the solution for $C_f$ is 
$$
C_f=\dfrac{C_s}{K}+(C_w-\dfrac{C_s}{K})e^{-z/L},
$$
where $C_w=91 uM$. The exponential factor is:
$$
L^{-1}=(\dfrac {v^2}{4D^2}+\dfrac{f_cRMK}{D})^{1/2}-\dfrac{v}{2D}.
$$
For each site, the value of $L$ can be obtained by fitting the Sr concentration profile with depth with two tunable parameters, $L$ and $C_s/K$. The best value for $L$ is then used in calculating recrystallization rate of calcite based on the following equation:
$$
R=(\dfrac{1}{L^2}+\dfrac{V}{LD})\dfrac{D}{f_cMK}
$$
where $M=1.1,K=20,D=7500 m^2/Myr$.

$f_c$ is calculated using the average calcite fraction in the top 200 meters of the sediments. $V$ is calculated using the average sedimentation rate for the sediments that are younger than 10 Myr. Compaction is not considered. Depth is fitted with age using a linear relationship to calculate the average sedimentation rate.

Site 1052 and 1053 do not have age data younger than 10 Myr. There seems to be no deposition of sediments in the recent 30 Myr. Their sedimentation rates are thus assigned zeros. Age data for Site 1092, 1238 and 1258 are not available. The sedimentation rates for these sites are estimated as follows: Site 1238 is ~ 70m/Myr sed rate. Site 1258 has early Eocene sediments at the top (more or less) so sed rate ~ 0. Site 1092 has variable sed rate, but averages about 15m/Myr down to about 180m depth.




Results
-------

|      |       L (m) | Sedimentation rate (m/Myr) | Calcite fraction (%) | Recrystallization rate (/Myr) |
| ---: | ----------: | -------------------------: | -------------------: | ----------------------------: |
|  803 |     74.3314 |                    16.3279 |              89.1611 |                     0.0804005 |
|  805 |     44.7164 |                    23.3704 |              91.0996 |                      0.213227 |
|  806 |     85.3729 |                    27.6493 |              91.0451 |                      0.067543 |
|  807 |     65.1849 |                    23.1772 |              91.7706 |                      0.105037 |
|  900 |     263.015 |                    13.6868 |              44.3815 |                     0.0164335 |
|  974 |     652.897 |                    37.9524 |              36.5062 |                    0.00942847 |
|  982 |     22.8844 |                    22.2051 |              80.5807 |                      0.862584 |
|  998 |     67.9886 |                    15.3758 |              71.8507 |                      0.116951 |
| 1052 | 4.40277e+06 |                          0 |              78.5214 |                   2.23975e-11 |
| 1053 | 1.37652e+06 |                          0 |              75.1237 |                   2.39496e-10 |
| 1085 | 2.59247e+06 |                    28.1973 |              70.0881 |                    7.0546e-07 |
| 1088 |     115.695 |                     12.782 |              91.1468 |                     0.0334521 |
| 1092 |     226.032 |                         15 |              80.1803 |                     0.0120842 |
| 1120 |     125.044 |                    7.95019 |              94.5484 |                     0.0261166 |
| 1169 |     182.614 |                    14.2235 |              84.8714 |                     0.0162166 |
| 1170 |     54.5796 |                    16.3783 |              86.9402 |                      0.147319 |
| 1194 |     84.7243 |                    10.5696 |              79.0856 |                      0.067222 |
| 1238 |      576.71 |                         70 |              53.7681 |                     0.0121674 |
| 1258 |     483.674 |                          0 |              49.2018 |                    0.00296178 |



![](/files/Sr.png)

![](/files/RecrysRateVsSediRate.png)

![](/files/RecrysRateVsCalcite.png)

Literature Cited
----------------



