<!--
 .. title: Will reservoirs be clogged by salt precipitation during CO2 dryout
 .. slug: ZhangLiu
 .. date: 2015-03-25 21:44:25 UTC-05:00
 .. tags: carbon sequestration, dry out, reservoir clogging
 .. link: 
 .. description: 
 .. type: text
 -->

Introduction
============

In CO$_2$ sequestration, well injectivity is a critical issue. The injected dry gas, at low water-vapor partial pressure, will equilibrate with the formation brine and water will evaporate into the flowing CO$_2$ stream. Water salinity increases as a result and eventually precipitates out salt. This effect has been reported for gas producing wells in reservoirs of high salinity brine [@kleinitz2003halite] and during storage of natural gas [@place1984unusual]. The source of extra pressure build-up in the Ketzin [@baumann2014monitoring] and Snohvit [@grude2014pressure] CO$_2$ storage projects is partly assigned to salt precipitation. Probably because few large-scale pilots have been built for CO$_2$ sequestration, direct observations of salt precipitation have not been available at field scale. Right now we rely on numerical simulations [@giorgis20072d; @pruess2009formation; @qiao2014compositional; @zeidouni2009analytical] and experimental studies [@pearce1996natural; @andre2014well; @ott2015salt; @roels2016capillary; @muller2009co2; @tang2015experimental; @wang2010halite] to determine the key parameters involved so that we can correctly model well injectivity on the field scale.

Field-scale simulations require input on flow physics such as the porosity-permeability relationship. Porosity change can be calculated simply from the volume of precipitated salt. The change of permeability, however, is a complex problem. The most widely used porosity-permeability relationship in current numerical simulations is the tube-in-series model proposed by [@verma1988thermohydrological]. This model allows to reach zero permeability even if porosity is not nil. In this model, pore geometry is conceptualized as a series of one-dimensional tubes that are identical to each other. Each tube consists of wide and narrow segments, and the permeability value is dominated by the local radii of the narrowest part of the tube. When salt precipitates on the tube walls, the local permeability for the narrow segments decreases much more rapidly than those for the wide segments. The result is clogging of the entire tube. [@pruess2009formation] used this relationship in their numerical simulator TOUGH2 [@pruess1991tough2] to explore the role of different parameters in the salt precipitation process and found that injectivity could be reduced significantly. For the given parameter values used in [@pruess2009formation], reservoir permeability is reduced to zero when precipitated salt occupies 10% of the pore space.

Most recent publications related to salt precipitation in CO$_2$ storage have used the [@verma1988thermohydrological] porosity-permeability relationship, but with different parameter values from fitting of experimental data [@andre2014well; @muller2009co2; @bacci2013experimental; @giorgis20072d; @guyant2015salt; @ott2015salt]. Exceptions are the papers by [@zeidouni2009analytical] and [@tang2015experimental] where they use the simple Kozeny-Carman grain model [@carman1956flow; @carman1997fluid] based on spheres to calculate changes in permeability due to changes in porosity. Recently, [@liu2013permeability] points out that the [@verma1988thermohydrological] relation between permeability change and salt precipitation is based on a single phase flow model, but CO$_2$ sequestration involves two phases. They conceptualize the porous media as a series of tubes with different sizes, and develop a new relation between permeability change and salt precipitation that considers the fact that salt precipitation occurs only in the pore space occupied by brine during the precipitation process. This model is in agreement with observations by [@ott2015salt] in which they conduct core flooding experiments and claim that there is no transport mechanism of liquid water vapor across the CO$_2$ brine interface and hence no transport mechanism of salt into the CO$_2$ flow channels. These CO$_2$ flow channels will stay open since salt precipitates in the residual brine phase.

Compared to the [@verma1988thermohydrological] model in which permeability change is a single function of porosity change, the [@liu2013permeability] model relates permeability change to not only porosity change, but also pore size distribution and water saturation at which precipitation takes place. The [@liu2013permeability] model is also a continuum-scale relation in that all parameters involved are available in current reservoir simulators. It is thus possible to implement this relation in a reservoir simulation code.

Intuitively, the [@liu2013permeability] model will predict less reduction in permeability compared to the [@verma1988thermohydrological] model given the same amount of salt precipitation since precipitation is limited to the water occupied pore space, and the pathways for CO$_2$ gas stay open. However, since fluid saturations and flow rates close to the well bore cover a large range as functions of time and space, there is no simple answer to how much the new porosity-permeability relationship will affect the simulation of CO$_2$ injection. To our best knowledge, no efforts have been made to explore the effects of different porosity-permeability relationships in field-scale numerical simulations. This paper implements the [@liu2013permeability] model in the reservoir simulator TOUGH2, and uses the example in [@pruess2009formation] as a case study to present the different implications of the two constitutive relations. Results show that the implementation of different permeability-porosity relations significantly affects temporal and spatial distributions of all hydraulic parameters, including solid saturation, permeability change, pressure, and gas saturation. In contrast to the conclusions from [@pruess2009formation] that salt precipitation will reduce well injectivity substantially, the [@liu2013permeability] model predicts much less reduction in permeability. Discussions are given at the end of this manuscript on the evaluation of each relation and the corresponding experimental evidences.




What porosity-permeability relationships are used in recent studies
-------------------------------------------------------------------

[@bacci2011experimental] conducted core flooding experiments with supercritical CO$_2$, and used the [@verma1988thermohydrological] model to fit the experimental data. The reduced porosities from several experiments were plotted against permeability reductions. However, readers need to note that in this plot each data point is an averaged porosity and permeability of the entire core. In most such experiments, salt precipitation is heterogeneous inside the core and more salt precipitates close to the injection zone. In numerical simulations of core flooding experiments, the core is discretized into a number of grid blocks. Porosity change is monitored in each grid block. The porosity-permeability relationship is also applied in each grid block to calculate the corresponding permeability change. Thus, the porosity-permeability relationship obtained from the average porosity and permeability measurements of the entire core does not necessarily represent the true porosity-permeability relationship for each grid cell, especially when salt precipitation has large variations through the core.

[@ott2015salt] used the same [@verma1988thermohydrological] model to fit their experimental data, but introduced a new term which was the lowest value to which permeability can be reduced by precipitation. They also argued that the maximum pore volume that could be filled by precipitate was the volume corresponding to the residual brine saturation, thus the critical porosity was 0.8 (assuming residual water saturation was 0.2). Using these constraints, they determined a rather large exponential term equal to 10.1.

[@giorgis20072d] used the [@verma1988thermohydrological] as a regression function to fit their extended Verma and Pruess model, and determined an exponential term equal to 4.1 and a critical porosity of 0.3. [@pruess2009formation] chose parameters similar to what was used in another study of permeability changes due to precipitation of amorphous silica at a geothermal injection well in the Philippines [@xu2004reactive], with the exponential term being equal to 2 and the critical porosity equal to 0.9.

[@tang2015experimental] and [@zeidouni2009analytical] used the simple Kozeny-Carman grain model based on spheres to calculated changes in permeability due to changes in porosity. [@zeidouni2009analytical] used the equation with no tunable parameters, while [@tang2015experimental] included an exponential coefficient and used experimental data to determine its value. Exponent 2.4 was demonstrated through the data regression with the minimum deviation.

[@mohamed2013fluid] used both the Carman-Kozeny relation and power law to fit experimental data. They found that the exponent terms cover a large range of values, from around 4 to as high as 400. The significant reduction of permeability corresponding to the large exponents are mainly because of the pore-throat plugging by fines migration due to the presence of silicate minerals in dolomite rock.

The relations above are listed in Table \[table:PoroPerm\] along with their parameter values, and plotted in Fig.\[fig:PoroPerm\]. It seems to us that, compared to other models, the [@liu2013permeability] model provides a more physics sound relation for porosity and permeability evolution, since it honors the physical process of salt precipitation in a two-phase system and is based on well-established relative permeability relationships.



## [@liu2013permeability] model

In [@liu2013permeability], the pore space of a porous medium is conceptualized as cylindrical capillaries with a continuous distribution of radii $r$. A given capillary can be either water-filled or completely dry, depending on the saturation state of the medium. With this geometric idealization, the capillary pressure-water saturation curve can be interpreted to represent continuous cumulative pore-size distribution (PSD). In a given portion of the porous medium (in computational terms this would be a cell within the modeled domain), at any time the water content is known. Due to precipitation/dissolution, the pore volume will change and thus the capillary pressure curve changes also. The maximum radius up to which pores are water-filled and therefore affected by mineral reactions can be calculated from capillary
pressure head:

$$r = \frac{1}{h},$$

where *r* is the threshold radius and *h* is the capillary pressure head. The corresponding effective water saturation *S* is defined as:

$$S=\frac{\theta-\theta_{r}}{\theta_{s}-\theta_{r}},$$

where $\theta$ is the wetting-phase content (the ratio of wetting-phase volume to the corresponding bulk volume of a porous medium), and subscripts *s* and *r* refer to saturated and residual values for $\theta$.

The capillary pressure head *h* is given as a function of effective wetting-phase saturation by @van1980closed:

$$S=[1+(\alpha h)^{n}]^{-m},$$

where $\alpha$ and *m=1-1/n* are empirical parameters.

Before mineral reactions, the relative permeability of the wetting phase *$k_{r}$* can be expressed by @mualem1976new:

$$k_r=S^{1/2} [\dfrac{\int_0^s (1/h(x))dx}{\int_0^1 (1/h(x))dx}]^2.$$

We have $$k_{r}(S)=S^{1/2}[1-(1-S^{1/m})^m]^2.$$

The changes in pore geometry during salt precipitation is a complex process. Here a strict dependency of salt precipitation on solution concentrations is assumed, in other words, the amount of precipitated salt in a given pore is linearly dependent on its pore volume. Also the change in pore volume is assumed to be uniform within a given pore.

Denoting the brine content and corresponding effective saturation at the time when mineral reaction starts as $\theta_p$ and $S_p$, the ratio of pore volume after chemical reactions to that before reactions, $\beta$, can be defined as

$$\beta=\dfrac{\theta_p-\theta_{salt}}{\theta_p},$$

where $\theta_{salt}$ is the content of precipitated salt, defined as the volume of salt precipitation divided by the bulk volume of a porous medium. The ratio $\delta$ of the hydraulic radius (for a pore after precipitation) to its original radius can be approximated to be a power function of the corresponding volume ratio [@liu2013permeability]:

$$\delta=\beta^{\chi},$$

where $\chi$ is an empirical parameter equal to 4.5.

In previous studies [@verma1988thermohydrological], changes in pore volume were modeled as affecting the entire pore spectrum despite the fact that salt precipitation occurs only in the water-filled pores. Here, instead, only changes in pore volumes in the wet part of the porous medium are translated to pore radii.

In a given portion of the porous medium, at any time the water saturation is known. The maximum radius up to which pores are water-filled and therefore affected by salt precipitation is calculated as: 

$$r_{p}=\alpha [S_p^{1/m}-1]^{-1/n}.$$ 

The radius $r_{p}$ divides the pore spectrum into a dry, inert part and a wet reactive part, which has to compensate for the change in pore volume. For the calculation of the new PSD, only the pore radii of the wet pore space are multiplied by the proportionality factor $\delta$.

The closed-form equation for permeability change due to mineral
reactions is given in [@liu2013permeability] as follows:

$$\dfrac{K}{K_0}=\tau^{1/2}(\delta-1)(1-(1-S_p^1/m)^m)+1]^2,$$

where $\tau$ is the tortuosity factor, and $\tau=1-S_p+\delta^2S_p$.

Compare with experimental measurements
--------------------------------------

Porosity-permeability relations fitted from experimental data provide empirical equations for field scale simulations, and sometimes such empirical relations are the most reliable options. However, due to the heterogeneity of salt precipitation in core flooding experiments, using the average porosity and permeability reduction measured for the entire core may not be a valid approach. Several experimental studies [@peysson2014well; @ott2015salt] have observed that the decrease in water saturation at the injection surface induces brine capillary back flow that transfers the brine toward the injection surface. Salt accumulates near the injection surface and precipitates when saturation is reached. In numerical simulations of such experiments, the representative element volume (REV) is defined as one thin slice of the core. In [@andre2014well], the 60 mm long core was represented by 60 grid cells, with each cell being 1.0 mm thick, and most salt precipitation accumulated in the first few millimeters of the core, close to the injection zone. The porosity-permeability relationship is an equation that describes the physics in each REV, which is the 1.0 mm slice in this case. Using the porosity and permeability data for the entire core to fit a porosity-permeability relationship is not conceptually consistent with the REVs in numerical models. In fact, the capillary back flow and precipitation of salt near the injection zone can be reproduced by continuum-scale numerical models with two-phase Darcy flow, capillary pressure, and thermodynamics of salt precipitation. The porosity-permeability relationship should not double account for the rapid permeability reduction by heterogeneous precipitation. Given the difficulty in measuring porosity and permeability change in each slice of a core sample, the best data for fitting the porosity-permeability relation comes from experiments where salt precipitation is homogeneous along the core. [@ott2015salt] found that there is a critical flow rate above which salt precipitates homogeneously. At high injection rate, the viscose force increases, and the capillary force becomes less important to drive back flow. Using a flow rate of 4.4 ml/min, they observed a uniform salt saturation of 0.04 throughout the core after drying. However, such experimental data is rare, and in most experiments heterogeneous precipitation of salt is observed [@peysson2014well; @andre2014well; @ott2015salt]. One other option is to deliberately cut off the zone close to injection inlet and examine the rest of the core where precipitation is relatively uniform. In order to measure the permeability of a fraction of the core, pressure needs to be measured not only at the inlet and outlet, but also along the core length at discrete locations. Such measurements can be achieved by using side taps as in the setup in [@wang2010halite].

@liu2013permeability used the experimental work by @wang2010halite to compare their predictions on permeability change with experimental observations. The flood experiments were performed on brine saturated cores that were 1.5 inch in diameter and 1 foot longe. [@liu2013permeability] selected the data for the core segment between two side taps (3cm-13.05cm) and avoided the zone near the injection inlet (0-3cm). The ratio of the new permeability for this segment after CO$_2$ dry-out to the initial permeability measured in the experiment is 0.55, and the value predicted from the [@liu2013permeability] model is between 0.50 and 0.57. The prediction from the [@liu2013permeability] model is indeed close to the experimental measurement.

Here we also calculate the predicted permeability ratio using the [@verma1988thermohydrological] model and compare it with the experimental measurement in [@wang2010halite]. In the laboratory test the salt mass fraction in brine $X_{salt}$ was 25.0%. The core was initially saturated with brine, and the breakthrough of supercritical CO$_2$ happened at about 0.3 pore volume (PV) of injection. Since the displaced brine had little time to interact with CO$_2$, it is reasonable to assume that there was no salt precipitation form the displaced brine, and the remaining brine in the core when precipitation starts was 0.7 PV. The brine production slowed down greatly after the breakthrough, and CO$_2$ continued to flood through the core for all the remaining brine to evaporate into. In total, about 176 PV of supercritical CO$_2$ was injected into the core. Thus, the amount of salt precipitation at the end of flooding is estimated to be

$$\dfrac{\rho_{aq}}{\rho_s} X_{salt} \times 0.7 PV = 0.0959 PV​$$

where $\rho_{aq}=1180kg/m^3$ is the aqueous phase density and $\rho_s=2153kg/m^3$ is the density of precipitated salt. Using Eq.\[eq:verma\] where $\phi / \phi_0=1-0.0959=0.9041,\phi_r=0.9$, we have $\dfrac{k}{k_0}=0.001681$. Obviously this overestimates the reduction of permeability compared to results using the [@liu2013permeability] model (0.50-0.57) and measured in the experiment (0.55).


Does salt precipitate in the aqueous phase?
-------------------------------------------

The key assumption in the [@liu2013permeability] relation is that salt precipitates in the water occupied pore space. The assumption is reasonable given that salt initially dissolves in water and can only precipitates out of water. [@ott2015salt] conducted core flooding experiments of CO$_2$ replacing brine in a sandstone sample and used micron CT to image the distribution of solid salt and the initial CO$_2$ in the pore space. Their 3D representation of the solid salt distribution and the early CO$_2$ percolation pattern showed that both patterns occupied complementary space and overlapped by less than 5% of the common cross section. This indicated that salt precipitated in the vicinity of the initially CO$_2$ occupied volume, leaving the initial CO$_2$ pathways essentially open. They thus claim that there is no transport mechanism of liquid water vapor across the CO$_2$-brine interface and hence no transport mechanism of salt into the CO$_2$ channels, and the flow channels stay open since salt precipitates in the residual brine phase.

[@miri2015new] conducted lab-on-chip experiments to explore the dynamics of salt precipitation at the pore-scale, and reached opposite conclusions. They found that salt aggregates attracted water from the adjacent network grains via continuous water films around the mineral grains through surface energy effects, and this enabled continued feeding of the evaporating front with fresh brine, thus allowing the
continued growth of salt on these aggregates. The result of this mechanism was a large accumulation of salt in the form of aggregates in the gas phase. An important requirement for this self-enhancing mechanism was the interconnected films that were relative thick on the surface of grains. However, the existence of such thick water film and their practical significance in hydraulic conductivity needs further investigation. The flow mechanism associated with this significant film flow is not considered in this study.


Conclusions
===========

This work highlights that the implementation of permeability-porosity relationships in reactive transport modeling can affect simulation results significantly. The conceptual model based on which constitutive relations are derived has to be consistent with the problem being modeled in a numerical code. In our case, the salt precipitation from water due to CO$_2$ dry-out involves two-phase flow. By implementing the @liu2013permeability model which is derived for two-phase flow systems, relatively mild reduction of permeability is predicted compared to the [@verma1988thermohydrological] model. Further work can be done to develop the relations that represent how multi-phase flow properties, for example capillary pressure, and relative permeabilities change after mineral reactions. This will provide the full set of chemical effects on flow properties for reactive transport modeling.

Systematic experiments are in need to validate the porosity-permeability relations proposed by [@verma1988thermohydrological] and [@liu2013permeability]. Such experiments should include measurement of porosity and permeability in well defined representative element volumes. Two mechanisms could cause severe reduction of core permeability, although this reduction should not be double accounted for by the porosity-permeability relation intended for the REVs as discussed above. One mechanism is the capillary driven back flow that transport brine to close to the injection surface. Pore space is thus filled with more salt at these locations. The other possible mechanism is a boundary effect at the injection surface. Since the brine at the injection surface is fully exposed to CO$_2$ gas, and initially the brine occupies all pore space at the injection surface, it is possible that this brine will all evaporate and leave the entire injection surface clogged. The core permeability will be zero with this one surface clogged.

Field observation of salt precipitation in CO$_2$ sequestration projects have not been reported yet, but will be invaluable once available. Such observations can be used to confirm whether salt precipitation is severe at the injection surface, and whether capillary back flow is important at conditions encountered in field operations.



  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Publication**             **Porosity-permeability relation**                                                                                                                                                                                **Relation type**
  --------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------
  [@pruess2009formation]      $\dfrac{k}{k_0}=(\dfrac{\phi/\phi_0-\phi_r}{1-\phi_r})^2,\phi_r=0.9$                                                                                                                                              Verma and Pruess

  [@andre2014well]            $\dfrac{k}{k_0}=(\dfrac{\phi/\phi_0-\phi_r}{1-\phi_r})^2,\phi_r=0.91$                                                                                                                                             Verma and Pruess

  [@ott2015salt]              $\dfrac{k}{k_0} =(\dfrac{\phi/\phi_0-\phi_r}{1-\phi_r})^\tau (1-k_c/k_0) +k_c/k_0,\phi_r=0.8, \tau=10.1, k_c/k_0=3.5 \times 10^{-3}$                                                                              Verma and Pruess

  [@giorgis20072d]            $\dfrac{k}{k_0}=(\dfrac{\phi/\phi_0-\phi_r}{1-\phi_r})^\tau,\phi_r=0.3,\tau=4.1$                                                                                                                                  Verma and Pruess

  [@zeidouni2009analytical]   $\dfrac{k}{k_0}=(\dfrac{\phi}{\phi_0})^3 (\dfrac{1-\phi_0}{1-\phi})^2,\phi_0=0.12$                                                                                                                                Carman-Kozeny

  [@wang2010halite]           $\dfrac{k}{k_0}=(\dfrac{\phi}{\phi_0})^c (\dfrac{1-\phi_0}{1-\phi})^2,c=2.4$                                                                                                                                      Carman-Kozeny

  [@mohamed2013fluid]         $\dfrac{k}{k_0}=(\dfrac{\phi}{\phi_0})^c (\dfrac{1-\phi_0}{1-\phi})^2,c=4.53\sim445.0$                                                                                                                            Carman-Kozeny

  [@mohamed2013fluid]         $\dfrac{k}{k_0}=(\dfrac{\phi}{\phi_0})^n,n=5.17\sim448.2$                                                                                                                                                         Power Law

  [@liu2013permeability]      $\dfrac{k}{k_0}=\tau^{1/2}[(\delta\beta-1)(1-(1-S_p^{1/m})^m)+1]^2,m=0.748,\beta=\dfrac{\theta_p-1+\phi/\phi_0}{\theta_p}, S_p=0.342 (\theta_p=0.5, \theta_r=0.24), \delta=\beta^{4.5}, \tau=1-S_p+S_p\delta^2) $  Liu et al.

