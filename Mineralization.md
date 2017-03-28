**Mineralization of carbon dioxide sequestered in volcanogenic sandstone
reservoir rocks **

**Shuo Zhang^1,2^, Donald J. DePaolo^1,2^, Tianfu Xu^2^ and Liange
Zheng^2^**

> ^1^Earth and Planetary Science Department, University of California,
> Berkeley, CA 94720-4767, USA
>
> ^2^Earth Sciences Division, Lawrence Berkeley National Laboratory,
> University of California, Berkeley, CA 94720, USA

**Abstract**

Geological storage of carbon dioxide in deep saline formations can
decrease the accumulation of CO~2~ in the atmosphere, and thus slow down
global warming. Most CO~2~ injected into subsurface rock formations is
expected to remain for a long time as either a separate supercritical
phase or in solution in brine; both forms present the possibility of
leakage back to the surface or other environmental impacts.
Mineralogical trapping of injected CO~2~ is more secure but usually
thought to be too slow to add significantly to sequestration security.
For quartz-rich sandstones (quartzarenite and arkose), only ca. 5
percent CO~2~ mineralization is achieved over 1000 to 10,000 years
([Audigane et al., 2007](#_ENREF_3)). However, if volcanogenic and other
sandstones that have larger amounts of reactive minerals were used for
storage, there could be a larger fraction of CO~2~ mineralized in a
shorter time. The limitation is that porosity and permeability tend to
decrease with increase of volcanic rock fragments (VRF), which limits
the rate at which CO~2~ can be injected. We evaluate these tradeoffs to
assess the feasibility of using volcanogenic sandstone to achieve secure
CO~2~ storage. Using relationships between VRF percent, porosity and
permeability from available geological data, the reactive transport code
TOUGHREACT was used to model the flow, transport, mineral reactions,
changes in fluid chemistry, and the rate and extent of CO~2~
mineralization over 1000 years during and after CO~2~ injection into a
sandstone reservoir. We use the models specifically to evaluate the
expected trade-off between higher reactivity and lower porosity and
permeability. A model volcanic fragment mineralogy is used (pyroxene and
feldspar mainly for which kinetic data are available) along with
conservative estimates for silicate and oxide mineral dissolution
kinetics and reactive surface area. Substitution of other more common
reactive minerals such as chlorite and amphibole would not significantly
change the results. The simulations show that in rocks with 10 to 20%
reactive minerals, as much as 80% CO~2~ mineralization could occur in
1000 years and still allow sufficient injectivity so that 1 megaton of
CO~2~ could be injected per year per well. The calculated mineralized
fraction depends on several factors, most notably the kinetics and
reactive surface area of dissolving silicates and the detailed
relationship of reactive mineral content to effective permeability and
injectivity.

**Keywords**

CO~2~ sequestration; CO~2~ mineralization; volcanogenic sandstones;
reactive transport modeling


Introduction
------------

The accumulation of CO~2~ in the atmosphere increases greenhouse forcing
and contributes to global warming. Because it is likely that fossil
fuels will continue to be a vital component of energy resources in the
next several decades, the emitted CO~2~ has to be dealt with in some
way. Geological carbon storage is one of the primary options to reduce
CO~2~ emission during the extended transition to carbon neutral energy
sources. Geological formations, especially deep saline aquifers are
promising for carbon storage due to their large potential storage
capacity and geographic extent. The success of this option will be
measured by the storage duration and the risk for leakage. Effective
CO~2~ storage requires that ≥99% of injected CO~2~ be retained in the
subsurface for &gt;1000 years ([Intergovernmental Panel on Climate
Change, 2005](#_ENREF_14)).

There are four so-called trapping mechanisms that contribute to
retention of CO~2~ in the subsurface during geological carbon
sequestration ([Intergovernmental Panel on Climate Change,
2005](#_ENREF_14)): (1) structural trapping, in which CO~2~ is trapped
as a single supercritical phase according to the structural lithology of
the storage zone, (2) capillary trapping, where CO~2~ is retained as
small (≤1mm) bubbles in pore space due to the fact that CO~2~ generally
does not wet mineral surfaces whereas saline brine does, (3) dissolution
trapping, which refers to CO~2~ that becomes dissolved in the ambient
liquid phase (brine), and (4) mineral trapping, which is CO~2~ that has
been incorporated into minerals due to chemical precipitation. Mineral
trapping is considered to be the most secure form of CO~2~ storage, but
is also slow to develop because it follows the slow release of cations
like Fe, Mg and Ca by dissolution of silicate and oxide minerals in the
rocks. The most likely candidate storage formations for CO~2~
sequestration are sedimentary rocks with relatively high porosity and
permeability, such as sandstones. The lithologies with the highest
porosity and permeability usually are rich in quartz (SiO~2~) with some
feldspar, and do not contain an abundance of silicate minerals that
contain divalent cations that can combine with CO~2~ to form carbonate
minerals (CaCO~3~, MgCO~3~, FeCO~3~). For sequestration in these types
of rocks, modeling studies have shown that only a few percent of
injected CO~2~ is trapped in minerals even after 1000 to 10000 years has
elapsed from the time of injection ([Audigane et al., 2007](#_ENREF_3)).

Dissolution of CO~2~ into the brine and subsequent formation of carbonic
acid is the first step in the mineral trapping mechanism. Carbon dioxide
dissolves slightly in water to form carbonic acid, which in turn can
slowly dissolve silicate minerals. Under appropriate conditions, the
divalent cations released by silicate mineral dissolution can combine
with dissolved carbonate ions to form stable carbonate minerals. This
mechanism, however, requires host rocks with a high acid neutralization
potential ([Baines and Worden, 2004](#_ENREF_5)). Rocks rich in calcium,
magnesium, and iron silicate minerals can neutralize acids by providing
Ca^2+^, Mg^2+^, Fe^2+^ that can form stable carbonate phases in the
presence of CO~2~ ([Gunter et al., 2000](#_ENREF_11)).

Igneous rocks, especially mafic and ultramafic rocks, are rich in
magnesium, iron, and calcium silicate minerals, and could theoretically
provide a high potential of mineral trapping by mineral carbonation
([Kelemen and Matter, 2008](#_ENREF_15)). However, plutonic igneous (and
metamorphic) rocks have negligible matrix permeability and porosity. The
permeability in such rocks is determined primarily by the presence, type
and orientation of fractures. Thus intrusive igneous and metamorphic
rock bodies are normally unpromising hosts for subsurface disposal or
sequestration of CO~2~, despite the apparently favorable rates of
chemical reactions.

Most extrusive igneous rocks are subject to similar limitations for the
disposal of CO~2~. The most extensive are flood basalts, found covering
large areas of the earth’s surface in certain parts of the world.
Basalts are commonly heavily fractured, and also possess rubble zones
and vesicle porosity. Both microcrystalline groundmass and residual
glass contain significant Ca, Mg and Fe. Therefore basalts could be
candidate host rocks for CO~2~ sequestration ([Matter et al.,
2007](#_ENREF_20); [McGrail et al., 2006](#_ENREF_21)). If the basalt
flows are buried and overlain by impermeable sedimentary cap rocks, they
could be favorable potential repositories of supercritical CO~2~,
particularly if tectonic deformation were to create structural traps.
However, the generally low permeability and porosity of the matrix would
suggest that CO~2~ injection rates would be limited, even if injectivity
could be enhanced by hydraulic fracturing. Furthermore, because
crystalline rocks do not contain a significant amount of indigenous
brine, reaction can only be achieved by injection of CO~2~-saturated
water (Matter et al., 2007). Since CO~2~ is sparingly soluble in H~2~O,
roughly 200 times the volume of fluid would need to be injected into the
rocks to store the same amount of CO~2~ that would be accomplished with
injection of pure supercritical CO~2~. This large volume of fluid
translates to the need for 200 times more injection wells, water, and
pore space. There are cases where ophiolite complexes are subjected to
severe hydrothermal alteration to serpentinites. Large amount of CO~2~
mineralization can be expected in these serpentinite-hosted aquifers and
serpentinized peridotites due to high reactivity of these rocks. The
upscaling of existing technologies that accelerate serpentinite
carbonation may prove sufficient for offsetting local industrial
emissions, however, global-scale implementation will require
considerable incentives and further research and development ([Power et
al., 2013](#_ENREF_26)){Power, 2013 \#1549}.

Volcanogenic sandstones with a relatively high percentage of volcanic
rock fragments (VRF) could be a promising target for CO~2~ sequestration
in that they have a sufficient percentage of reactive minerals to allow
substantial mineralization of injected CO~2~, but can also be porous and
permeable enough to allow injection at acceptable rates. The potential
shortcoming is that sediments with high VRF fractions tend to be more
heavily modified during burial diagenesis, including more compaction and
secondary mineral precipitation in pore space, and hence tend to have
decreased porosity and permeability ([Remy, 1994](#_ENREF_29)). However,
volcanogenic sandstones are potential or actual petroleum reservoirs in
a number of locations ([Summer and Verosub, 1992](#_ENREF_36)), which
indicates that there are instances where porosity and permeability are
high enough for oil recovery. Several porosity-enhancing natural
mechanisms such as framework-grain dissolution, devitrification of glass
at shallow depths, precipitation of early cements that retard
compaction, and fracturing have been identified in volcanogenic
sandstones ([Hawlader, 1990](#_ENREF_12)). These processes can produce
volcanogenic sandstone formations that are deeply buried but still
relatively porous and permeable. Questions remain concerning how common
these porosity-enhancing processes are, and our understanding of the
major controls on the diagenesis of volcanogenic sandstones is
incomplete.

In this study, we evaluate, using model rock compositions and measured
hydrological properties of sandstones taken from the literature, how
volcanic rock fragment abundance will affect the amount of CO~2~ that
can be injected from a single well and mineralized in a flat-lying 40
meter-thick sandstone reservoir. The reactive transport code TOUGHREACT
is used to calculate the amount of CO~2~ that can be injected and
trapped in minerals, the timescale over which such mineralogical
trapping would occur, and how the total amount of mineralized CO~2~
varies as a function of rock porosity, permeability and mineralogy. Key
uncertain parameters are reactive surface area and residual gas
saturation, so sensitivity tests are conducted with varying values for
these parameters.


Problem Setup
=============


Mineralogy of sandstone
-----------------------

To mineralize injected CO~2~, the requirement is that there be
sufficient Ca, Mg and Fe available to combine with CO~2~ to form
carbonate minerals, and also that these divalent cations be held in
minerals that dissolve relatively rapidly so that the cations are
released into solution on a time scale of hundreds of years. In general,
those minerals that contain Ca, Mg and Fe in large proportions are also
the minerals that dissolve fastest in the presence of acidic aqueous
solutions, so there is a correlation between the amount of available
cations and the rapidity with which the cations will become available.

Our approach is to evaluate model sedimentary rock compositions that
involve mixtures of quartz, alkali feldspar, and basaltic minerals such
as plagioclase feldspar and pyroxene, plus iron-titanium oxides. The
anorthite component of plagioclase is a source of Ca ions, and the
“diopside” and orthopyroxene are sources of Mg, Fe, and additional Ca.
Oxide minerals are mainly a source of Fe. This specific mineralogy we
use for the simulations is not typical of most volcanogenic sandstones,
but we use for illustrative purposes because the dissolution kinetics of
these minerals is relatively well studied. In most volcanogenic sands,
the divalent cation-bearing minerals are more likely to be chlorite,
zeolites, smectite, amphibole, and devitrified lithic fragments that may
still contain some of the original igneous minerals such as those we are
using for our model composition. The simulations using typical igneous
minerals provide us with generalizable results that we can apply in a
qualitative way to other sandstone mineralogies.

For our modeling purposes we use an idealized basaltic rock composition
for the mineralogy of VRF based on the mineralogy of the Palisades Sill,
which is holocrystalline and consequently the mineralogy can be
specified better than for volcanic rocks that contain devitrified glass
and poorly crystalline groundmass. Matter et al. ([2007](#_ENREF_20))
presented a dolerite analysis from the contact zone between the
Palisades Sill and the underlying Newark Basin sediments. The dolerite
is rich in Ca-bearing plagioclase and pyroxenes (augite and
orthopyroxene) and free of olivine. The whole rock chemistry and
observed mineralogy based on thin section analysis of the dolerite are
summarized in Table 1. The mineralogy used in the model is determined
from normative calculation as shown in Table 2 from the elemental
chemistry, because for the purposes of the model we need to separate out
the (Mg,Fe) and (Na,Ca) endmembers as separate minerals, although we use
the same dissolution kinetics for the solid solution endmembers. The
value of Fe^3+^/ (total iron) is assumed to be 0.2. Apatite and chromite
are ignored since they are present in very small amounts. The diopside
in our model is different from the “diopside” of normative calculation
in that the diopside in our model only has Mg and Ca, and has no Fe as
in the diopside from the normative calculation. This will cause some
differences in results but they should not change the conclusions
because Mg and Fe are playing similar roles.

Our strategy is to use the Palisades sill mineralogy as our “volcanic
rock fragment” composition, and then to use natural sandstone samples
that contain mafic volcanic rock fragments to evaluate the relationships
between VRF content and hydrological parameters. Sandstone samples from
the Tangbe formation of north central Nepal ([Durr and Gibling,
1994](#_ENREF_9)) are used as models for sandstone mineralogy (Table 3).
Volcaniclastic grains are characteristic of Tangbe sandstones, which
classify as lithic arenites. The lithic volcaniclastic grains (Lv) are
separated into two major groups on the basis of their mineral
composition and texture. Mafic grains Lv(M) represent basaltic fragments
according to their chemistry. Felsic grains Lv(F), on the other hand,
are mainly composed of quartz, plagioclase and K-feldspar (with the
ratio of 0.52:0.35:0.13). From their modal composition, felsic grains
represent rhyolite and dacite. A small number of volcanic grains Lv(Ch)
fits neither group. These grains are made up of material with a
chert-like appearance but a characteristic dark brown stain. Feldspar
laths in these lithic grains enable classification as volcanogenic
grains. For the purposes of calculation of silicate dissolution rates,
the Lv(M) component of the sandstones is assumed to have a modal
mineralogy the same as the normative mineralogy of the Palisades Sill
basalt.


Relationships between volcanic rock fragment percent, porosity and permeability
-------------------------------------------------------------------------------

Several processes can affect porosity during diagenesis of volcanogenic
sandstones, including early diagenesis (early leaching by fresh meteoric
water, compaction, authigenic mineral precipitation, cementation of
first-generation clays and burial dissolution) and late diagenesis
(late-stage cements, dissolution of framework grains or cement during
structural deformation). The diagenetic processes are controlled by a
number of factors, such as depositional environment, detrital
mineralogy, grain size, pore-water chemistry, temperature, pressure, and
burial history ([Remy, 1994](#_ENREF_29)). Porosity is strongly
influenced by detrital mineralogy. Remy ([1994](#_ENREF_29)) showed that
rocks with abundant VRF experienced the most compaction, hence had
decreased post-compaction porosity (which equals current macroporosity
plus cement and can be considered as the remaining porosity after early
compaction but before cementation). Cements vary in mineralogy.
First-generation chloritic mixed-layer clays are most abundant in
volcaniclastic petrofacies, whereas first-generation illite-smectite and
calcite are most abundant in nonvolcaniclastic petrofacies, so the
relationship between the extent of cementation and VRF is not easy to
generalize. Also uncertain is the production of secondary porosity due
to dissolution as a function of VRF. In rocks rich in VRF and with very
low initial porosities, pore-water circulation is severely restricted,
thereby preventing significant dissolution of framework grains. In rocks
rich in VRF and with relatively high porosity, the presence of
chemically-unstable lithic fragments promotes the formation of secondary
porosity. The complexities of diagenesis make it difficult to predict
permeability based on original sandstone mineralogy or any other single
compositional or textural parameter. Ultimately, because it is
impossible to specify permeability accurately even if porosity is known,
we vary permeability over a small range to evaluate its importance in
determining the outcome of the simulations.

As one approach to representing the effect of VRF abundance on rock
porosity, we used the empirical relationships Eq. 1 and Eq. 2 from Bloch
([1991](#_ENREF_6)) to calculate porosity and permeability from
mineralogy.

*Porosity = -6.1+9.8(1/sorting) +0.17rigid grain content* (1)

*Log~10~Perm =-4.67+1.34grain size+4.08(1/sorting) +0.0342rigid grain
content* (2)

Here “sorting” is the Trask sorting coefficient ([Trask et al.,
1932](#_ENREF_37)), “perm” is permeability in millidarcys, and “grain
size” is grain diameter in millimeters. The two equations were obtained
by fitting the data from Yacheng field, South China Sea. The model has a
large amount of independent information, and a high coefficient of
determination (R^2^=0.75 for porosity and 0.86 for permeability). All of
the fitted sample data lie within a 95% confidence interval of predicted
values as shown in Bloch (1991) (figure 14 and figure 15), although
these limits are large enough to significantly affect the performance of
potential reservoirs in a CO~2~ sequestration scenario.

The empirical equations from Bloch (1991) imply that porosity and
permeability are affected by mineralogical variables (rigid grain
content) and textural variables (grain size and sorting). Since the
objective is to evaluate the effect of mineralogy on rock porosity and
permeability, we assigned typical values to textural variables. The
Trask sorting coefficient is given a value of 1.5 for well to moderately
sorted sandstone, and grain size is assigned as 0.8 mm. Since the
calibration data set is based on wells with similar temperature and
pressure histories, post-depositional parameters (temperature, pressure,
time) are not incorporated in these models. So all the uncertainties in
textural variables (sorting and grain size) and post-depositional
parameters (temperature, pressure, time) are gathered in the constants
calculated with sorting coefficient =1.5 and grain size =0.8. Below we
see that these values lead to slightly smaller permeabilities than
expected from field data, and this is compensated by generating another
permeability set that covers slightly larger permeability values.

Another approach to evaluating mineralogy-permeability relations is to
use natural sandstones where there are sufficient characterization data
to evaluate the variability as well as the overall trends. Gibson-Poole
et al. ([2008](#_ENREF_10)) presented porosity and permeability data
from Gippsland Basin in southeast Australia. The data for the Kingfish
Formation sediments are reprinted here in Fig. 1. The porosities are
mostly in the range 10% to 30% and the permeabilities vary from about
0.1 to 10,000 mD. The majority of the points lie in the 15-30% porosity
and 10-10,000 mD permeability ranges. The empirical formula generated by
determining a best fit to these data is:

![](media/image1.emf) (3)

where *k* is permeability in mD and *φ* is porosity. According to this
equation, at least 8.6% porosity is needed to provide a minimum
permeability (i.e. 1md) for injection. Clearly this relationship has
limited applicability because the permeability can vary by a factor of
over 100 for the same porosity. Nevertheless, we use this relationship
as a reference, and use equations 1 and 2 and the mineralogy of the
Tangbe sedimentary rocks to calculate porosity and permeability. These
calculated values all lie close to but below the best-fit line of the
Kingfish Formation porosity-permeability data.

Our conclusion is that equations 1 and 2 give a reasonable estimate of
porosity-permeability relations in arenites, but that the large spread
in permeability at all porosities means that no one
porosity-permeability curve can adequately represent the likely range in
natural reservoirs. To account for this range, and to evaluate the
effect of permeability, we use two sets of permeability values. Those
calculated directly from Equations 1 and 2 are noted as “low
permeability,” and another set of porosity-permeability data (“high
permeability”) is also used in our model where all permeabilities are
increased by 5 times. This additional set of permeability data is
beneficial in that the relationship between VRF and permeability is key
to this study and the two data sets allow us to illustrate the large
effect of the permeability-porosity relationship. Our selected range of
values is nevertheless small in comparison to the likely natural range
as illustrated in Fig. 1. Further discussion of permeability and its
effects is provided in the Results section.


Hydrogeological setting and model
---------------------------------

The mafic volcanic rock fragment percent of the Nepal samples ranges
from 1.6% to 32.3%. Reservoir porosities and permeabilities are
calculated for each sample and then listed in Table 4. Brine
compositions are obtained by pre-equilibrating 1.0 mol/L NaCl saline
water with the respective corresponding mineral assemblage for 10 years.
All simulations are run initially with a 1-D model with radial symmetry.
The model is therefore in some sense a 2-D model, but we refer to it as
1-D because the fluids are not allowed to segregate vertically due to
buoyancy forces. We have run 2-D radial models as well, and the
differences between 1-D and 2-D models are relatively small and
discussed further below. Initial reservoir pressure is set at constant
200 bar with a formation temperature of 75 ^o^C. This temperature is
calculated for a depth of 2 km, given a land surface temperature of 15
^o^C and a geothermal gradient of 30 ^o^C/km. Formation thickness is set
to 40m. Continuous injection is assumed to take place over a period of
100 years at a constant injection rate of 1 megaton CO~2~ per year. For
the lower reservoir permeabilities that are associated with our model
rocks with higher VRF, injection pressure needs to be increased to
achieve the same injection rate of 1 Mt/yr. We set a maximum injection
pressure of 390 bar (39 MPa). In cases where the reservoir permeability
is too low to allow injection of 1 Mt/y CO~2~ at this injection
pressure, the injection pressure is set at 39 MPa and the rate is
decreased to be consistent with the permeability. Geochemical transport
simulations are continued until 1000 years; an arbitrary cutoff chosen
to limit the computational time for the models and to allow us to
compare the amount of CO~2~ mineralized in a specified amount of time.


Modeling Approach
=================


Simulation method
-----------------

Simulations are conducted using the nonisothermal reactive transport
code TOUGHREACT V2 ([Xu and Pruess, 2001](#_ENREF_41)). This code
introduces reactive chemistry into the existing multiphase fluid and
heat flow code TOUGH2 ([Pruess, 1991](#_ENREF_27)). A new fluid property
module, ECO2N, is used based on the work by Spycher and Pruess
([2005](#_ENREF_34)). ECO2N provides an accurate description of the
thermophysical properties of water and CO~2~ mixtures under conditions
typically encountered in saline aquifers for CO~2~ disposal (10 ^o^C ≤ T
≤110 ^o^C; P ≤ 600 bars).

Fluid and heat flow processes considered in this code are: (1) fluid
flow of liquid and gas phases under pressure and gravity forces, (2)
capillary pressure effects for liquid phases, and (3) heat flow by
conduction, convection and diffusion. Transport processes that affect
aqueous and gaseous species are advection, molecular diffusion and
hydrodynamic dispersion. For our simulations, chemical reactions between
dissolved aqueous species and gas (i.e. supercritical CO~2~) are assumed
to be locally at equilibrium (although TOUGHREACT V2 can consider
aqueous species kinetics). Mineral dissolution and precipitation are
subject to kinetic limitations.

The space discretization in our modeling is based on the integral finite
difference (IFD) method ([Narasimhan and Witherspoon,
1976](#_ENREF_24)). This method allows the use of unstructured grids,
which is well suited for simulation of flow, transport, and fluid-rock
interactions in heterogeneous and fractured rock systems with varying
petrology, and hence provides flexible discretization of geologic media.
For regular grids, the IFD method is equivalent to the conventional
finite difference method.

TOUGHREACT uses a sequential iteration approach for calculations of
flow, transport, and kinetic geochemical reactions (but noniterative
between transport and chemistry). After solving flow equations,
velocities and saturations of the aqueous phase are used for aqueous
chemical transport calculations. Chemical transport is solved on a
component basis. Resulting concentrations obtained from the transport
and CO~2~ gas pressures from multiphase flow calculation are then
substituted into a chemical reaction model. The system of chemical
reaction equations is solved on a grid-block basis by Newton-Raphson
iteration.

An automatic time step control is used for the flow calculation. Time
step size is doubled if convergence occurs within 4 Newton-Raphson
iterations. The starting time step is 1 second and the upper limit for
time step size is set to be 5 days. For transport equations, a
stabilized bi-conjugate gradient solver is used. No limit of the time
step size for chemical reactions is included.


Flow and transport model setup 
-------------------------------

The specific model we used for our calculation is a 1-D model with
distance *d* ranging from 0 m to 100 km, which can be considered as
infinitely long.

For boundary conditions, there is no flow at both *d*=0m and *d*=10^5^m.
For fixed injection pressure condition, the first grid is assigned an
infinitely large volume (10^50^m^3^) and a gas saturation of 100% so
that it serves as a CO­­~2~ source and its properties don’t change
during the simulation. For the fixed injection rate condition, the
injection well is also located in the first grid. Since the distance is
large enough to be considered infinite in the model, the right end
boundary condition is equal to an open end although there is no flow at
d=10^5^m. For initial conditions, the temperature is set to be 75 ^o^C
and the pressure is 200 bar. Initial gas saturation is zero and the
formation is filled with all brine. Initial brine compositions are
obtained by pre-equilibrating 1.0mol/L NaCl saline water in a batch
model for 10 years with minerals that are used later for reactive
transport modeling. Water chemistry is not changing after 10 years,
which indicates that a steady state fluid composition has been reached
under pre-injection conditions.

The equations for calculating relative permeability and capillary
pressure and corresponding parameters are listed in Table 5. They are
all from Van Genuchten([1980](#_ENREF_38)). Changes in porosity and
permeability due to mineral dissolution and precipitation are taken into
account in our model. Changes in porosity during the simulation are
monitored by tracking changes in mineral volume fractions. We chose a
simple grain model of Kozeny-Carman to calculate changes in permeability
due to changes in porosity, although the actual porosity-permeability
correlation in geologic media depends on a complex interplay of many
factors such as pore size distribution, pore shapes, and connectivity.
The Kozeny-Carman equation relates permeability *k* (in m^2^) to
porosity (φ) by

![](media/image2.wmf){width="1.1284722222222223in" height="0.475in"} (4)

where R~0~ is the initial local spherical close-pack radius. Hence, the
ratio of permeability *k* to initial permeability *k*~0~ can be
expressed as

![](media/image3.wmf){width="1.3263888888888888in" height="0.475in"} (5)

where φ­~0~ is the initial porosity. Since porosity decreases are of
order 10% of initial porosities during the course of the simulations,
and the initial porosities average about 16.8%, the typical permeability
change over 1000 years is *k/k*~o~ ≈ 0.68. Using the fitted
porosity-permeability relationship from Gibson-Poole et at.
([2008](#_ENREF_10)) presented earlier, the ratio of final permeability
and initial permeability *k/k*~o~ is 0.52 (initial porosity= 16.8%,
final porosity= 15.0%), which is in the same order with the result from
the Kozeny-Carman model used in the simulation. Considering the several
orders of magnitude of permeability range and the deviation in
determining the porosity-permeability relation from geological data, the
error caused from using the Kozeny-Carman equation is negligible.

For species transport, the diffusion coefficient for aqueous species is
set to be 10^-9^ m^2^/s. The diffusion coefficient is then multiplied by
the tortuosity and liquid saturation. The diffusion coefficient of the
medium for gaseous species is 10^-5^m^2^/s. Tortuosity is calculated
internally from the Millington and Quirk ([1961](#_ENREF_22)) model,
which is listed in Table 6.


Geochemical data
----------------

The reaction rate expression used in this paper is based on the
transition state theory (TST) ([Steefel and Lasaga, 1994](#_ENREF_35)):

![](media/image4.wmf){width="1.1881944444444446in"
height="0.5743055555555555in"} (6)

where *r* is the kinetic rate (positive values indicate dissolution, and
negative values indicate precipitation), *k* is the rate constant (moles
per unit mineral surface area and unit time) which is temperature
dependent, *A* is the specific reactive surface area per gram of
mineral, *Q* is the reaction quotient, and *K* is the equilibrium
constant for the mineral-water reaction written for the destruction of
one mole of mineral, whose values originated from the EQ3/6 V7.2b
database ([wolery, 1992](#_ENREF_40)). The parameters *θ* and *η* must
be determined by experiment, but are commonly set to unity when
experimental quantification is not available. Precipitation of secondary
minerals is represented using the same kinetic expression, although as
noted below this is a simplification for which there is little
justification other than lack of more detailed information.

[]{#OLE_LINK2 .anchor}The kinetic rate constant *k^T^* (where *T* is the
temperature in Celsius) can be summed from three mechanisms ([Palandri,
2004](#_ENREF_25)):

![](media/image5.wmf) (7)

where subscripts *nu*, *H*, and *OH* indicate neutral, acid, and base
mechanisms respectively, *E* is the activation energy, *k*^25^ is the
rate constant at 25°C, *R* is gas constant, *T* is absolute temperature,
*a* is the activity of species, and n is a constant power term.

[]{#OLE_LINK3 .anchor}Mineral dissolution and precipitation rates are a
product of the kinetic-rate constant, the reactive surface area and the
affinity term (1-*Q/*K), which describes how far the system is from
equilibrium, as represented by Eq. 6. The parameters used for the
kinetic rate expression are given in Table 6. We included separate rate
constants (*k~25~*), activation energies (*E*), and reaction orders
(*n*) for processes catalyzed by H^+^ and OH^-^. At any pH, the total
rate is the sum of the rates from all mechanisms. However, catalysis by
H^+^ or OH^-^ is only considered for mineral dissolution, not for
precipitation. Parameter values for the rate law were taken from
Palandri ([2004](#_ENREF_25)), who compiled and fitted experimental data
reported by many investigators. Solid solution effects are not
considered in this study. To make up for this deficiency, the kinetic
parameters of end members of each solid solution are set equal to the
*slowest* one, e.g. anorthite is set to albite; ferrosilite is set to
enstatite; and smectite-Na is set to smectite-Ca. These simplifications
are conservative but all potentially significant. We have not attempted
to evaluate each one independently because that would result in an
unwieldy number of simulations and would affect the results in
reasonably predictable ways (e.g. faster dissolution kinetics will allow
for more dissolution per unit time and hence more mineralization).

If the aqueous phase supersaturates with respect to a potential
secondary mineral, a small volume fraction of 1×10^-6^ is used for
calculating seed surface area for the new phase to grow. Possible
secondary minerals that are considered in this model are listed in Table
7. Precipitation of secondary minerals is represented using the same
   kinetic expression as that for dissolution. However, several aspects of
   precipitation are different from dissolution, such as nucleation and
   crystal growth. Some authors have argued that dissolution and
   precipitation are fundamentally identical but opposite in sign ([Dove et
   al., 2008](#_ENREF_8)), whereas others provide evidence that there are
   pronounced differences. The kinetics of dissolution are more likely to
   be important for the results presented here, and it is clear that all
   reactive transport models are simple representations of what are likely
   to be complex relationships that depend on solution composition in ways
   that are not reflected by just the degree of saturation of the
   particular mineral under consideration. The complications relating to
   mineral precipitation are not considered in the current model. Since
   precipitation rate data for most minerals are unavailable, only
   parameters for neutral pH rates were employed to describe precipitation.
   Multiple kinetic precipitation mechanisms can be specified in an input
   file of the TOUGHREACT program, should such information become
   available.

Mineral reactive surface areas (RSA) are based on the work of Sonnenthal
et al. ([2005](#_ENREF_33)), and are calculated assuming a cubic array
of truncated spheres constituting the rock framework. In conformity to
White and Peterson ([1990](#_ENREF_39)) and Zerai et al.
([2006](#_ENREF_43)), a surface roughness factor of 10 is incorporated
and defined as the ratio of true surface area to equivalent geometric
surface area. Interaction with minerals is generally expected to occur
only at selected sites of the mineral surface, and the actual RSA could
be one to three orders of magnitude less than the surface
roughness-based surface area due to coating or armoring ([Zerai et al.,
2006](#_ENREF_43)). To account for these effects, the actual RSA are
decreased by 100 times from the surface roughness-based surface areas.
The RSA used here (9.8 cm^2^/g) for most minerals are similar to those
used by Zerai et al. (2006). Clay minerals are assigned much larger RSAs
(151.6 cm^2^/g) due to small particle size.

To provide the reactive surface area in the unsaturated system corrected
by rock/water ratio, the surface area of each mineral (in units of
m^2^~mineral~/kg~water~), which is internally calculated, is given by:

![](media/image6.wmf)

Where A~r~ is the reactive surface area in units of
m^2^/m^3^~fracture\ medium~, f~m~ is volume fraction of the mineral,
ρ~w~ is the density of water (in kg/m^3^), φ~f~ is porosity of the
medium, S~w­~ is water saturation, S~m­~ is the minimum liquid
saturation for which water-rock reactions are considered. S~m~ was set
to a small saturation (e.g. 1x10^-4^) in our model, to ensure that
reactions take place until virtually no water is left since water is the
wetting phase during CO~2~ sequestration.

Typically in reactive transport modeling a representative element volume
is a well-mixed homogenous block. So here we don’t treat the volcanic
rock fragments and the rest of the sandstone as two spatially separate
materials in one grid block. Instead the effects of volcanic fragments
on the properties of the grid blocks are taken into account in two ways.
First, the percentages of volcanic rock fragments are used to calculate
porosity and permeability of the whole sandstone. Second, the rock
fragment percentages are used to calculate the percentages of reactive
minerals; these reactive minerals are then embedded in the rock
homogenously with RSA=9.8 cm^2^/g which is the same as the other
minerals in the sandstone. In this approach, we are assuming that the
rock fragments have the same porosity, permeability and RSA as the rest
of the rock. These assumptions represent the simplest possible approach,
but may be justified for our purposes. For example, we have examined
volcanic sandstone samples from the Echegoin Formation near Coalinga,
California (thin section picture shown in Figure 2). The volcanic
fragments of this sandstone have similar sizes as the other mineral
grains, which should give similar RSAs for reactions. Also the volcanic
fragments are mostly equally distributed in the sandstone, which is
reasonable support for our assumption of homogeneous porosity and
permeability.


Results
=======

As described in section 2, we selected 5 volcanogenic sandstone samples
from Central Nepal that have chemical and mineralogical data available.
Porosities and permeabilities were calculated for each sample using
empirical equations generated from the Yacheng field. Another set of
permeability data was generated by multiplying the original ones by 5 to
cover a larger range of permeability values, but a range that is still
small in comparison to the full range of possible permeabilities as
represented by the Gibson-Poole et al. ([2008](#_ENREF_10)) data (Figure
1). Injection rate is fixed at 1 megaton per year for samples with a
large permeability that requires no larger than 390 bar injection
pressure, whereas samples with low permeabilities that would need more
than 390 bar were set at constant injection pressure of this maximum
value and thus had less than 1 Mt/yr of CO~2~ injected. All samples were
run with the reactive transport code TOUGHREACT using a 1-dimensional
(radial) model. The simulations generated results for the distance that
the CO~2~-bearing fluid would flow, how much CO~2~ is mineralized, and
how system properties such as gas saturation and pH are distributed
along the flow path.


Relationships between VRF and CO~2~ mineralization amount
---------------------------------------------------------

The relationships between the amount of mineralized CO~2~ and %VRF are
presented in Fig. 3 and Fig. 4. For the Low Permeability case, sample 1
and sample 2 have injection rates of 1 Mt/yr while samples 3-5
(progressively higher VRF) are fixed at constant injection pressure of
390 bar since they would need a pressure higher than 390 bar to achieve
1 Mt/yr and we assume that standard injection equipment can achieve an
injection pressure only as high as 390 bar. As permeability decreases
from sample 2 to sample 5, the amount of injected CO~2~ decreases.
However, since the amount of reactive VRF increases from sample 1 to
sample 5, a larger percent of injected CO~2~ is mineralized. The
trade-off between increasing reactivity and decreasing permeability
generates an optimal case at VRF ≈ 6% where the amount of mineralized
CO~2~ has the largest value. For the High Permeability case, the amount
of injected CO~2~ and mineralized percent show similar patterns as those
in the Low Permeability set, but the optimal case shifts from 6% to
somewhere between 10% and 21% VRF. Thus it can be seen that the amount
of mineralized CO~2~ depends on how we determine permeabilities from
mineralogy, or more generally the relationships between mineralogy,
porosity and permeability. Nevertheless, the results suggest that if
formations can be identified that have relatively high VRF and modest
permeability, mineralization of injected CO~2~ can be almost
quantitative over a timescale of 1000 years.

Fig. 5 shows the evolution of total sequestered CO~2~ in the mineralized
phase, aqueous phase and supercritical phase for the entire reservoir in
the case of 21% VRF in the High Permeability case. CO~2~ injection is
conducted for 100 years and then stopped. Supercritical CO~2~ phase
dominates at first and then decreases rapidly after injection ceases,
first due to dissolution into the aqueous phase, and then due to
mineralization. The amount of aqueous CO~2~ increases first until it
reaches saturation in water; its value stays roughly stable until about
700 years. Overall, supercritical CO~2~ first dissolves in the aqueous
phase, and then reacts with cations in the aqueous phase released by
mineral dissolution and produces carbonate precipitation. About 78% of
injected CO~2~ is mineralized, 6% remains in the aqueous phase, and 16%
remains as the supercritical phase at time = 1000 years.


Radial distribution of system properties for the optimal case
-------------------------------------------------------------

The radial distribution of reservoir pressure, gas saturation, pH,
porosity, and CO~2~ sequestration amount per medium volume are presented
in Fig. 6a – 6e. The CO~2~ - affected region is limited within a radial
distance of 4500m-6000m except for pressure. In our 2-fluid phase 1-D
model, the primary variables are pressure, temperature, gas phase
saturation and salt mass fraction. The pressure near injection well as
shown in Fig. 6a is 390 bar from the beginning to 100 years, when CO~2~
is injected into the formation. Pressure decreases further way from the
injection well, and the affected distance reaches 60 km, where the
hydrostatic pressure is 200 bar. The high pressure decays after
injection ceases at 100 years and already returns to hydrostatic
pressure at 200 years. Gas saturation is close to 100% within 200 meters
from the CO~2~ injection well at the time of 100 years, which means that
water is almost completely replaced by supercritical CO~2~. Further away
from the injection well, supercritical CO~2~ phase and water phase
coexist, where the gas saturation decreases from 1 to 0 as shown in
Figure 6b. Mutual dissolution of CO~2~ and water is also considered and
calculated in the model. Subsequently supercritical CO~2~ dissolves into
the brine and is consumed by mineralization, so the gas saturation line
moves down after 100 years, which indicates a decrease of gas saturation
in the system. At the same time, water gradually flows back
spontaneously due to the suction of water by the rock (capillary
pressure). This process of spontaneous flow of the wetting phase into
porous media is called imbibition. Gas saturation and water saturation
add up to 1 at any time and at all places.

The pH decreases from 8.0 to 5.0 close to the injection well due to
CO~2~ injection. The low pH induces accelerated mineral dissolution due
to the increase in dissolution rate at low pH. The track along which the
pH line moves is similar with that in the gas saturation graph. The line
moves forward during the first 100 years, and gradually moves backward
during the next 900 years, which indicates that a large amount of CO~2~
is mineralized subsequent to 100 years when water flows back. Porosity
decreases from the original value of 0.168 to 0.150 at 1000 years. This
decrease happens because CO~2~ mass is added to the solid matrix by rock
alteration. The change in porosity reduces permeability to 77% of its
original value according to Eq. 5. The total mineralized CO~2~ reservoir
per unit volume keeps increasing monotonically during the whole time
period. After 1000 years, the value reaches about 37 kg/m^3^. This value
would keep increasing if the simulation were not stopped.


Mineral alteration and aqueous phase composition of the optimal case
--------------------------------------------------------------------

Minerals and aqueous species with significant changes of abundance are
presented in Fig. 7a, 7b and 8. The minerals of the model volcanic rock
fragment (pyroxene mainly) all dissolve significantly. As these minerals
dissolve, the concentrations of Mg, Fe, and Ca are all increased in the
aqueous fluid, and pH is also increased, eventually leading to
precipitation of secondary phases. Some of the injected CO~2~ is
immobilized by precipitation of three carbonate minerals: magnesite,
ankerite and calcite. Precipitation of ankerite is due to ferrosilite
dissolution to provide Fe^2+^. Magnesite and calcite precipitation is
due to the dissolution of anorthite, enstatite and diopside components
to provide Ca^2+^ and Mg^2+^. Some Ca^2+^ and Mg^2+^ remain in the
aqueous phase. There is also significant precipitation of quartz, and
significant dissolution of anorthite and precipitation of albite. Minor
precipitation of K-feldspar, siderite and dawsonite with abundance
changes in the order of 10^-5^ also occur but are not plotted due to
their small values. The decrease in pore volume is attributable largely
to the fixation of CO~2~ into mineral phases and secondarily to the fact
that the replacement minerals have lower average density than the
primary minerals used for the calculation.


Discussion and implications
===========================

Our simulations suggest that volcanogenic sandstones may be attractive
reservoir rocks for geologic carbon sequestration. Volcanogenic
sandstones have the advantage of high reactivity as in basalt and
peridotite, but are in other respects typical porous sandstones that
would allow for deep injection of supercritical CO~2~ rather than
shallow injection of carbonated water as in Kelemen and Matter
([2008](#_ENREF_15)). The results of our simulation study, which is
based on a combination of observed properties of impure sandstones and a
model mineralogy including up to 30% by volume of reactive, divalent
cation-bearing minerals, a 40m-thick homogeneous formation with a radius
of 5000 m could accommodate injection of 85 megatons of supercritical
CO~2~ through a single well in 100 years, with 77 percent of the
injected CO~2~ being converted to carbonate minerals within 1000 years.
Because CO~2~ storage will only be justifiable if injected CO~2~ stays
immobilized in the subsurface for thousands of years, this high
percentage of mineralization would be attractive.

Typical volcanogenic sandstones are mixtures of mineral grains and
volcanic and sub-volcanic rock fragments ([Ingersoll, 1983](#_ENREF_13);
[Linn et al., 1992](#_ENREF_19)). To simulate the reactive behavior of
volcanic rock fragments we have used a combination of minerals, mainly
pyroxenes and feldspar, for which laboratory dissolution rate data are
available. In general we have used conservative values for dissolution
rate constants and reactive surface area. Nevertheless, the critical
control on the percentage of mineralization that can be achieved is the
relationship between the volume fraction of reactive minerals (or the
fraction of volcanic rock fragments) and permeability. The models
suggest that &gt;50% mineralization could be achieved within 1000 years
in formations containing at least 10% VRF and a permeability of about 60
mD. We assume, and there are some data in the literature to bear this
out, that permeability declines as VRF increases. With this assumption,
there is a trade-off between higher reactivity and lower permeability
with increasing VRF. But for any reactive mineral content, there is a
range of permeabilities that are likely as a result of variable
diagenetic histories and proportions of cements. For our low
permeability cases, permeability drops off quickly at high VRF, which
means that the total amount of CO~2~ that can be injected per well is
small, and hence the optimum condition for mineralization occurs at low
%VRF. For our high permeability cases, the optimum condition shifts to
about 15 to 20% VRF, and much more CO~2~ can be both injected and
mineralized.


Reactive surface area
---------------------

The evaluation of reactive surface area (RSA) in natural geologic media
is complex, especially for multi-mineral systems, and has not yet been
described in a manner that would allow accurate estimation for a given
mineralogy and porosity. RSA calculated from grain size is often a poor
estimate of the hydrologically accessible mineral surface area. The
specific RSA may vary over several orders of magnitude depending on
grain size, mineralogy, surface roughness, coatings, weathering, and
biological effects.

Sensitivity tests with respect to RSA are based on the optimal case with
21% VRF in the high permeability set. Two additional simulations were
performed by respectively increasing and decreasing all RSAs uniformly
by a factor of 5, which is arbitrarily chosen. The RSAs for secondary
minerals are changed by the same factor. Results in Fig. 9 show that RSA
has a direct effect on the rate of CO~2~ mineralization. The amount of
injected CO~2~ also changes, but very slightly, so only the original
injection line is plotted. Varying RSA between 2cm^2^/g and 50cm^2^/g
changes the mineralized fraction from 29% to 95% at 1000 years. In the
RSA= 50 cm^2^/g case, reaction is very fast and the CO~2~ mineralization
reaches its maximum at about 400 years and stops increasing afterwards.


 Residual gas saturation
------------------------

Residual gas saturation (RGS) was shown to play an important role in
storing CO~2~ by Kumar et al.([2004](#_ENREF_2); [2004](#_ENREF_17)). In
our baseline model a value of 0.10 was assigned to RGS, which is
consistent with experimental measurements by Kitamura et al.
([2006](#_ENREF_16)). In the sensitivity tests a smaller value of 0.05
and a larger value of 0.2 are arbitrarily chosen for comparison.
However, such values are both possible from core scale measurements or
previous models ([Andre et al., 2006](#_ENREF_1); [Bachu and Bennion,
2008](#_ENREF_4)). Fig. 10 shows that small values of RGS lead to
increased mineralization of CO~2~. This increase comes about because a
greater amount of gas remains mobile, which leads to increased contact
between CO~2~ and brine. In terms of relative permeability, a smaller
value of residual gas saturation gives larger values of the relative
permeability of supercritical CO~2~ phase, especially in low gas
saturation zones. The exact equation that describes the relationship
between gas relative permeability and residual gas saturation used in
this study can be found in Table 5. Thus more CO~2~ can be injected into
the formation for smaller residual gas saturation due to larger gas
permeability. About 95 Mton of CO~2~ is injected into the formation in
100 years with an injection pressure of 390 bar for RGS=0.05, while only
85 Mton of CO~2~ can be injected at the same pressure with RGS = 0.2.
Also, CO~2~ flows farther for smaller residual gas saturations and
occupies a larger volume of the domain. For example, the pH front for
RGS=0.1 is at 6000 meters at 100 years as shown in Figure 6c, while the
pH front of RGS=0.05 is around 9000 meters. So, the volume of rocks that
are exposed to CO~2~ is larger for smaller RGS values. For our model,
the rate-controlling step of mineralization is the dissolution of mafic
minerals, which is measured in moles of minerals per unit time per unit
volume of rock. With similar dissolution rates, the amount of
mineralized CO~2~ is thus proportional to the volume of rock that is
involved in reactions with CO~2~, and increases with smaller values of
RGS.


Mineralogy and trapping efficiency
----------------------------------

Minerals that are sources of divalent cations and common in impure
sandstones are biotite, chlorite, glauconite, amphibole, epidote, and
montmorillonite. Chlorite and montmorillonite are common alteration
products of volcanic glass, and VRF are commonly composed of
combinations of such minerals as well as devitrified glass that is
effectively amorphous. Available data suggest that the dissolution rates
of these minerals are not much different from those used for our
simulations. However, they may critically affect the types of secondary
minerals formed and the ability for CO~2~ to be sequestered by
carbonates due to the different types of secondary minerals, and their
effect on permeability. Nevertheless, to first order it appears that the
specific mineralogy is less important than the amount of reactive
minerals. It is also noteworthy that minerals such as chlorite and
montmorillonite could have significantly higher reactive surface areas
than the values we are using ([Landrot et al., 2012](#_ENREF_18)).

As shown in Table 6, typical dissolution rate constants for divalent
cation-bearing silicates are near 10^-10^ mol/m^2^/sec at temperature of
75 ^o^C, which translates to about 0.003 mol/m^2^/y. This number has
also included the acceleration by the acid mechanism as indicated by
Equation 7, and will approximate the actual dissolution rate if the
solutions are moderately far from equilibrium. If a rock contains 10
volume percent of a mineral with density of 2800 kg/m^3^ and specific
surface area of 1 m^2^/kg, 1m^3^ of such rock would contain 280 m^2^ of
reactive surface area. With these numbers, the predicted timescale of
mineral dissolution would be about 1000 years; or in other words roughly
2/3 (actually 1 – e^-1^) of the reactive mineral inventory would
dissolve in 1000 years. Assuming a molecular weight similar to feldspar
(about 280 g/mol), about 600 moles of reactive mineral would be
dissolved in 1000 years. For comparison, if 5 to 10% of the rock volume
is initially filled with CO~2~ at a density of 600 kg/m^3^, then the
1m^3^ volume contains about 30 to 60 kg of CO~2~ or about 680 to 1360
moles of CO~2~. Hence the release of cations from mineral dissolution
over 1000 years is approximately enough to mineralize 40 to 90 percent
of the capillary-trapped CO~2~.

The above calculation is significant because it implies that the
reaction rate and reactive mineral fraction of reservoir rocks are the
critical parameters for assessing mineralization of injected CO~2~. It
also shows that slight changes in the rates can have a large effect on
the result. If dissolution rates are retarded by 10x, there will likely
be 10x less mineralization over 1000 years. And if the rates could be
enhanced, there would be significant benefit in terms of increasing the
amount of mineralized CO~2~.

Audigane et al (2007) used a reactive transport model to estimate the
relative fractions of capillary trapped, dissolved, and mineralized
CO~2~ in the Utsira Formation, a quartz-rich sandstone that is being
used as a reservoir formation for the Sleipner CO~2~ sequestration
project. In their simulation, they calculate that only 1-2% of the CO~2~
is mineralized after 1000 years. This small amount of calculated
mineralization is consistent with the fact that they had only 1.3% by
volume of reactive mineral (Fe-rich chlorite), and that the conversion
of CO~2~ to FeCO~3~ (about 20 mol/m^3^ by 1000 years) was offset by a
similar amount of CO~2~ release by dissolution of calcite.

Our simulations suggest that the mineralogical trapping efficiency of
impure sandstones can be reduced to a relatively simple parameter that
involves permeability, reactive mineral percentage and residual CO~2~
saturation:

![](media/image7.wmf)

where X~rm~ is the volume fraction of reactive minerals containing
divalent cations, and s~g~ is the residual gas saturation for CO~2~ in
brine. The approximate sign applies because the ratio of densities and
molecular weights is close to unity for typical minerals and
supercritical CO~2~. This ratio is effectively a ratio of the number of
divalent cations available per unit volume of reservoir rock to the
number of CO~2~ molecules present as capillary-trapped bubbles. If X~rm~
/ s~g~ ≥ 1, then a large fraction of injected CO~2~ can be expected to
be mineralized. For our simulations that produce high mineralization
fractions in 1000 years this ratio is in the range 1 to 2. If reaction
rates are higher or lower than assumed in our models, it will not
greatly affect the fraction of CO~2~ mineralized, but it will affect the
timescale over which the mineralization happens. The remaining
significant parameter is the injectivity, which scales roughly with
permeability. Hence, in economic terms, the figure of merit would be:

![](media/image8.emf){width="1.0791666666666666in"
height="0.48541666666666666in"}

If this number is high, it will maximize the amount of CO~2~ that can be
injected and expected to mineralize in 1000 years *per injection well*.
Based on our simulations, more than half of injected CO~2~ could be
mineralized with an injection rate of 1 MT CO~2~/yr for formations where
this number is ≥50 mD.

**5.4 Fractures, heterogeneity, and 2-D effects**

A critical component of our analysis is the formation injectivity for
CO~2~. Our models assume that injectivity is directly determined by the
core-scale permeability, which may be an overly conservative assumption.
In most cases, the effective permeability at the scale of injection
(10’s of meters) can be 1 or even 2 orders of magnitude higher than the
core-scale permeability ([Raghavan, 2006](#_ENREF_28)). This difference
is usually attributed to larger scale heterogeneity, including the
presence of fractures, and tends to be more significant in rocks with
lower permeability. If this scale dependence effect were taken into
account, it would greatly enhance the potential for mineralization. In
terms of our figure of merit, sandstones with much lower permeability
could still be effective storage targets. One additional factor that
will be important, however, is how mineralization and dissolution will
affect the fracture permeability ([Sausse et al., 2001](#_ENREF_32)).

Formation heterogeneity can also affect both hydrology and geochemical
evolution during sequestration. If, for example, a formation has
mineralogical heterogeneity, and if permeability decreases as reactive
minerals increase as we assumed in our model, then during injection,
flow will be concentrated in the regions of high permeability (low
%VRF). This would mean that during injection, much of the CO~2~ will be
separated from the reactive minerals, with the separation distances
being similar to the length scales that characterize the permeability
heterogeneity. This effect might increase mineralization. The high
permeability zones will enhance the injectivity and allow more CO~2~ to
be injected into the formation per unit time per well. In the early
stages of system evolution there is some separation of CO~2~ from
reactive minerals, but on longer time scales, the CO~2~ (and or H^+^)
will be able to diffuse into the reactive zones. Assuming that the
effective diffusivity of CO~2~ D ≈ 0.23 m^2^/yr at 100°C([Zeebe,
2011](#_ENREF_42)), the diffusion lengthscale in 100 years L~d~ ≈
(4Dφt)^0.5^= 3 meters, and in 1000 years is about 10 meters. Thus, the
low pH conditions in the high-permeability zones will penetrate the low
permeability zones if the scale of the heterogeneity (mostly vertical
heterogeneity), is of order a few meters or less. The overall effect may
be positive as injectivity will be increased but reactivity on a
1000-year time scale will remain similar. As noted by Bryant et al.
([2006](#_ENREF_7)), permeability heterogeneity may also enhance
structural and capillary trapping of CO~2~.

Although the calculations we present are 1-dimensional (quasi
2-dimensional because they are radially symmetric), the results do not
change much when the extra (vertical) dimension is added. Simulations
done using a 2-D (quasi 3-D) allow for buoyancy effects, which allow the
CO~2~ to rise upward toward the caprock and spread somewhat farther. It
also results in more contact area between CO~2~ and brine, and hence
somewhat faster dissolution of CO~2~ into brine and slightly more
extensive mineral-rock interaction. The overall effect is to allow
somewhat more CO~2~ (ca. 18% more) to be mineralized as shown in Figure
11.


Conclusions
===========

As a potential target lithology for CO~2~ sequestration, volcanogenic
sandstone has both the advantage of high reactivity as in basalts and
peridotite, reasonable injection rates as in standard sandstones, and
contains native brine so that pure supercritical CO2 can be injected.
According to this simulation study, a 40 m thick homogeneous formation
with a radius of 5000 m is able to achieve an injection of 85 megatons
CO~2~ in 100 years and mineralization of about 80% injected CO~2~ at
1000 years.

There is a trade-off for geochemical trapping of CO~2~ between higher
reactivity and lower permeability with increasing volcanic rock fragment
fractions. The key relationship is between mineralogy and permeability.
For Low Permeability, the peak of mineralized CO~2~ amount lies at less
than 10% VRF, while for slightly higher Permeability, it shifts to
around 10-20%. Reactive surface area and residual gas saturation affect
the rate of CO~2~ sequestration significantly. Sensitivity tests are
conducted for these parameters.

Further work is necessary to better constrain the critical parameters
that control the rate and extent of carbon mineralization; a direct
means to this end would be to conduct experiments with volcanic
sandstone samples in supercritical CO~2~ saturated brine to measure
CO~2~ mineralization rates. It would also be beneficial to identify
volcanogenic sandstone formations that are suitable for CO~2~
sequestration projects and evaluate the sequestration potential of such
formation by field characterization. .Two such formations that are
worthy of study are the Haizume and Tomokomai formations of onshore and
offshore Japan, which are being used for CO~2~ injection experiments
(cf. Mito et al., ([2008](#_ENREF_23)) ; .Sato et
al.,([2011](#_ENREF_31)))

**Acknowledgement**

This manuscript has benefited from discussions with Eric Sonnenthal,
Jenny Druhan and the comments of two anonymous reviewers. The work was
supported by the Director, Office of Science, Office of Basic Energy
Sciences of the U.S. Department of Energy as part of an Energy Frontier
Research Center under Contract No. DE-AC02-CH11231.

**References**

[]{#_ENREF_1 .anchor}Andre, L., AUDIGANE, P., AZAROUAL, M., MENJOZ, A.,
2006. Numerical modeling of fluid-rock chemical interactions at the
supercritical CO2-liquid interface during CO2 injection into a carbonate
reservoir, the Dogger aquifer (Paris Basin, France). Energ Convers
Manage 48, 1782-1797.

[]{#_ENREF_2 .anchor}Armstrong-Altrin, J.S., Lee, Y.I., Verma, S.P.,
Ramasamy, S., 2004. Geochemistry of sandstones from the upper Miocene
Kudankulam Formation, southern India: Implications for provenance,
weathering, and tectonic setting. J Sediment Res 74, 285-297.

[]{#_ENREF_3 .anchor}Audigane, P., Gaus, I., Czernichowski-Lauriol, I.,
Pruess, K., Xu, T.F., 2007. Two-dimensional reactive transport modeling
of CO2 injection in a saline Aquifer at the Sleipner site, North Sea. Am
J Sci 307, 974-1008.

[]{#_ENREF_4 .anchor}Bachu, S., Bennion, B., 2008. Effects of in-situ
conditions on relative permeability characteristics of CO2-brine
systems. Environ Geol 54, 1707-1722.

[]{#_ENREF_5 .anchor}Baines, S.J., Worden, R.H., 2004. The long-term
fate of CO2 in the subsurface: natural analogues for CO2 storage.
Geological Society, London, Special Publications 233, 59-85.

[]{#_ENREF_6 .anchor}Bloch, S., 1991. Empirical prediction of porosity
and permeability in sandstones.

[]{#_ENREF_7 .anchor}Bryant, S.L., Lakshminarasimhan, S., Pope, G.A.,
2006. Buoyancy-Dominated Multiphase Flow and Its Effect on Geological
Sequestration of CO2. Spe J 13, 447-454.

[]{#_ENREF_8 .anchor}Dove, P.M., Han, N., Wallace, A.F., De Yoreo, J.J.,
2008. Kinetics of amorphous silica dissolution and the paradox of the
silica polymorphs. Proceedings of the National Academy of Sciences.

[]{#_ENREF_9 .anchor}Durr, S.B., Gibling, M.R., 1994. Early Cretaceous
Volcaniclastic and Quartzose Sandstones from North Central Nepal -
Composition, Sedimentology and Geotectonic Significance. Geol Rundsch
83, 62-75.

[]{#_ENREF_10 .anchor}Gibson-Poole, C.M., Svendsen, L., Underschultz,
J., Watson, M.N., Ennis-King, J., van Ruth, P.J., Nelson, E.J., Daniel,
R.F., Cinar, Y., 2008. Site characterisation of a basin-scale CO2
geological storage system: Gippsland Basin, southeast Australia. Environ
Geol 54, 1583-1606.

[]{#_ENREF_11 .anchor}Gunter, W.D., Perkins, E.H., Hutcheon, I., 2000.
Aquifer disposal of acid gases: modelling of water-rock reactions for
trapping of acid wastes. Appl Geochem 15, 1085-1095.

[]{#_ENREF_12 .anchor}Hawlader, H.M., 1990. Diagenesis and reservoir
potential of volcanogenic sandstones--Cretaceous of the Surat Basin,
Australia. Sediment Geol 66, 181-195.

[]{#_ENREF_13 .anchor}Ingersoll, R.V., 1983. Petrofacies and provenance
of late Mesozoic forearc basin, Northern and Central California. Aapg
Bull 67, 1125-1142.

[]{#_ENREF_14 .anchor}Intergovernmental Panel on Climate Change, 2005.
IPCC special report on carbon dioxide capture and storage : summary for
policymakers. IPCC, S.l.

[]{#_ENREF_15 .anchor}Kelemen, P.B., Matter, J., 2008. In situ
carbonation of peridotite for CO2 storage. P Natl Acad Sci USA 105,
17295-17300.

[]{#_ENREF_16 .anchor}Kitamura, K.X., Z., 2006. An experimental study of
Residual Gas Saturation of Carbon Dioxide in water-saturated porous
sandstone by using multi-channel seismic wave imaging method. American
Geophysical Union, Fall Meeting 2006, abstract \#H51E-0531.

[]{#_ENREF_17 .anchor}Kumar, M. Noh, G.A. Pope, K. Sepehrnoori, S.
Bryant, L.W. Lake, 2004. Reservoir Simulation of CO2 Storage in Deep
Saline Aquifers. SPE/DOE Symposium on Improved Oil Recovery, 22-26 April
2006, Tulsa, Oklahoma, USA.

[]{#_ENREF_18 .anchor}Landrot, G., Ajo-Franklin, J.B., Cabrini, S.,
Steefel, C.I., 2012. Measurement of the reactive surface area relevant
to CO2 mineralization in a reservoir sandstone. Chem Geol 318-319,
113-125.

[]{#_ENREF_19 .anchor}Linn, A.M., Depaolo, D.J., Ingersoll, R.V., 1992.
Nd-Sr Isotopic, Geochemical, and Petrographic Stratigraphy and
Paleotectonic Analysis - Mesozoic Great Valley Fore-Arc
Sedimentary-Rocks of California. Geol Soc Am Bull 104, 1264-1279.

[]{#_ENREF_20 .anchor}Matter, J.M., Takahashi, T., Goldberg, D., 2007.
Experimental evaluation of in situ CO2-water-rock reactions during CO2
injection in basaltic rocks: Implications for geological CO2
sequestration. Geochem Geophy Geosy 8, Q02001.

[]{#_ENREF_21 .anchor}McGrail, B.P., Schaef, H.T., Ho, A.M., Chien,
Y.J., Dooley, J.J., Davidson, C.L., 2006. Potential for carbon dioxide
sequestration in flood basalts. J Geophys Res-Sol Ea 111.

[]{#_ENREF_22 .anchor}Millington, R.J., Quirk, J.P., 1961. Permeability
of porous solids. Transactions of the Faraday Society 57, 1200-1207.

[]{#_ENREF_23 .anchor}Mito, S., Xue, Z., Ohsumi, T., 2008. Case study of
geochemical reactions at the Nagaoka CO2 injection site, Japan. Int J
Greenh Gas Con 2, 309-318.

[]{#_ENREF_24 .anchor}Narasimhan, T.N., Witherspoon, P.A., 1976. An
integrated finite difference method for analyzing fluid flow in porous
media. Water Resour. Res. 12, 57-64.

[]{#_ENREF_25 .anchor}Palandri, J.K., Y.K., 2004. A compilation of rate
parameters of water-mineral interaction kinetics for application to
geochemical modeling. US Geol. Surv. Open File Report2004-1068, 64pp.

[]{#_ENREF_26 .anchor}Power, I.M., Wilson, S.A., Dipple, G.M., 2013.
Serpentinite Carbonation for CO2 Sequestration. Elements 9, 115-121.

[]{#_ENREF_27 .anchor}Pruess, K., 1991. TOUGH2: A general-purpose
numerical simulator for multiphase fluid and heat flow, p. Medium: ED;
Size: Pages: (102 p).

[]{#_ENREF_28 .anchor}Raghavan, R., 2006. Some observations on the scale
dependence of permeability by pumping tests. Water Resour. Res. 42,
W07402.

[]{#_ENREF_29 .anchor}Remy, R.R., 1994. Porosity Reduction and Major
Controls on Diagenesis of Cretaceous-Paleocene Volcaniclastic and
Arkosic Sandstone, Middle Park Basin, Colorado. J Sediment Res A 64,
797-806.

[]{#_ENREF_30 .anchor}Rutqvist, J., Tsang, C.-F., Stephansson, O., 2000.
Uncertainty in the maximum principal stress estimated from hydraulic
fracturing measurements due to the presence of the induced fracture. Int
J Rock Mech Min 37, 107-120.

[]{#_ENREF_31 .anchor}Sato, K., Mito, S., Horie, T., Ohkuma, H., Saito,
H., Watanabe, J., Yoshimura, T., 2011. Monitoring and simulation studies
for assessing macro- and meso-scale migration of CO2 sequestered in an
onshore aquifer: Experiences from the Nagaoka pilot site, Japan. Int J
Greenh Gas Con 5, 125-137.

[]{#_ENREF_32 .anchor}Sausse, J., Jacquot, E., Fritz, B., Leroy, J.,
Lespinasse, M., 2001. Evolution of crack permeability during fluid‚rock
interaction. Example of the Brzouard granite (Vosges, France).
Tectonophysics 336, 199-214.

[]{#_ENREF_33 .anchor}Sonnenthal, E., Ito, A., Spycher, N., Yui, M.,
Apps, J., Sugita, Y., Conrad, M., Kawakami, S., 2005. Approaches to
modeling coupled thermal, hydrological, and chemical processes in the
Drift Scale Heater Test at Yucca Mountain. Int J Rock Mech Min 42,
698-719.

[]{#_ENREF_34 .anchor}Spycher, N., Pruess, K., 2005. CO2-H2O mixtures in
the geological sequestration of CO2. II. Partitioning in chloride brines
at 12-100°C and up to 600 bar. Geochim Cosmochim Ac 69, 3309-3320.

[]{#_ENREF_35 .anchor}Steefel, C.I., Lasaga, A.C., 1994. A Coupled Model
for Transport of Multiple Chemical-Species and Kinetic Precipitation
Dissolution Reactions with Application to Reactive Flow in Single-Phase
Hydrothermal Systems. Am J Sci 294, 529-592.

[]{#_ENREF_36 .anchor}Summer, N.S., Verosub, K.L., 1992. Diagenesis and
organic maturation of sedimentary rocks under volcanic strata, Oregon.
Aapg Bull 76, 1190-1199.

[]{#_ENREF_37 .anchor}Trask, P.D., Hammar, H.E., Wu, C.-c.e., American
Petroleum, I., 1932. Origin and environment of source sediments of
petroleum. American Petroleum Institute, Houston.

[]{#_ENREF_38 .anchor}Van Genuchten, M.T., 1980. A closed-form equation
for predicting the hydraulic conductivity of unsaturated soils. Soil
Science Society of America Journal 44, 892-898.

[]{#_ENREF_39 .anchor}White Art, F., Peterson Maria, L., 1990. Role of
Reactive-Surface-Area Characterization in Geochemical Kinetic Models,
Chemical Modeling of Aqueous Systems II. American Chemical Society, pp.
461-475.

[]{#_ENREF_40 .anchor}wolery, T.J., 1992. EO3/6:Software package for
geochemical modeling of aqueous systems: Package overview and
installation guide (version 7.0). Lawrence Livermore Natioinal
Laboratory Report UCRL-MA-210662 PT I.

[]{#_ENREF_41 .anchor}Xu, T., Pruess, K., 2001. Modeling Multiphase
Non-isothermal Fluid Flow and Reactive Geochemical Transport in Variably
Saturated Fractured Rocks: 1. Methodology. Am J Sci 301, 16-33.

[]{#_ENREF_42 .anchor}Zeebe, R.E., 2011. On the molecular diffusion
coefficients of dissolved CO2 and their dependence on isotopic mass.
Geochim Cosmochim Ac 75, 2483-2498.

[]{#_ENREF_43 .anchor}Zerai, B., Saylor, B.Z., Matisoff, G., 2006.
Computer simulation of CO2 trapped through mineral precipitation in the
Rose Run Sandstone, Ohio. Appl Geochem 21, 223-240.
