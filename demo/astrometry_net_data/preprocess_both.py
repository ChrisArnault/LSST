<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>
<head>
<title>contrib/demos/lsst_dm_stack_demo.git - DM stack demos for end users
</title>
<meta name='generator' content='cgit v0.9.0.2-39-g756e'/>
<meta name='robots' content='index, nofollow'/>
<link rel='stylesheet' type='text/css' href='/cgit.static/cgit.css'/>
<link rel='alternate' title='Atom feed' href='http://dev.lsstcorp.org/cgit/contrib/demos/lsst_dm_stack_demo.git/atom/astrometry_net_data/preprocess_both.py?h=master' type='application/atom+xml'/>
</head>
<body>
<div id='cgit'><table id='header'>
<tr>
<td class='logo' rowspan='2'><a href='/cgit/'><img src='/cgit.static/cgit.png' alt='cgit logo'/></a></td>
<td class='main'><a href='/cgit/'>index</a> : <a title='contrib/demos/lsst_dm_stack_demo.git' href='/cgit/contrib/demos/lsst_dm_stack_demo.git/'>contrib/demos/lsst_dm_stack_demo.git</a></td><td class='form'><form method='get' action=''>
<select name='h' onchange='this.form.submit();'>
<option value='Winter2012'>Winter2012</option>
<option value='master' selected='selected'>master</option>
<option value='tickets/1989'>tickets/1989</option>
</select> <input type='submit' name='' value='switch'/></form></td></tr>
<tr><td class='sub'>DM stack demos for end users
</td><td class='sub right'></td></tr></table>
<table class='tabs'><tr><td>
<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/'>summary</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/refs/'>refs</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/log/astrometry_net_data/preprocess_both.py'>log</a><a class='active' href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/astrometry_net_data/preprocess_both.py'>tree</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/commit/astrometry_net_data/preprocess_both.py'>commit</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/diff/astrometry_net_data/preprocess_both.py'>diff</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/stats/astrometry_net_data/preprocess_both.py'>stats</a></td><td class='form'><form class='right' method='get' action='/cgit/contrib/demos/lsst_dm_stack_demo.git/log/astrometry_net_data/preprocess_both.py'>
<select name='qt'>
<option value='grep'>log msg</option>
<option value='author'>author</option>
<option value='committer'>committer</option>
<option value='range'>range</option>
</select>
<input class='txt' type='text' size='10' name='q' value=''/>
<input type='submit' value='search'/>
</form>
</td></tr></table>
<div class='path'>path: <a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/'>root</a>/<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/astrometry_net_data'>astrometry_net_data</a>/<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/astrometry_net_data/preprocess_both.py'>preprocess_both.py</a></div><div class='content'>blob: e403eabf810c5d7b43dbdaa9d852e3b86d21778f (<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/plain/astrometry_net_data/preprocess_both.py'>plain</a>)
<table summary='blob content' class='blob'>
<tr><td class='linenumbers'><pre><a class='no' id='n1' name='n1' href='#n1'>1</a>
<a class='no' id='n2' name='n2' href='#n2'>2</a>
<a class='no' id='n3' name='n3' href='#n3'>3</a>
<a class='no' id='n4' name='n4' href='#n4'>4</a>
<a class='no' id='n5' name='n5' href='#n5'>5</a>
<a class='no' id='n6' name='n6' href='#n6'>6</a>
<a class='no' id='n7' name='n7' href='#n7'>7</a>
<a class='no' id='n8' name='n8' href='#n8'>8</a>
<a class='no' id='n9' name='n9' href='#n9'>9</a>
<a class='no' id='n10' name='n10' href='#n10'>10</a>
<a class='no' id='n11' name='n11' href='#n11'>11</a>
<a class='no' id='n12' name='n12' href='#n12'>12</a>
<a class='no' id='n13' name='n13' href='#n13'>13</a>
<a class='no' id='n14' name='n14' href='#n14'>14</a>
<a class='no' id='n15' name='n15' href='#n15'>15</a>
<a class='no' id='n16' name='n16' href='#n16'>16</a>
<a class='no' id='n17' name='n17' href='#n17'>17</a>
<a class='no' id='n18' name='n18' href='#n18'>18</a>
<a class='no' id='n19' name='n19' href='#n19'>19</a>
<a class='no' id='n20' name='n20' href='#n20'>20</a>
<a class='no' id='n21' name='n21' href='#n21'>21</a>
<a class='no' id='n22' name='n22' href='#n22'>22</a>
<a class='no' id='n23' name='n23' href='#n23'>23</a>
<a class='no' id='n24' name='n24' href='#n24'>24</a>
<a class='no' id='n25' name='n25' href='#n25'>25</a>
<a class='no' id='n26' name='n26' href='#n26'>26</a>
<a class='no' id='n27' name='n27' href='#n27'>27</a>
<a class='no' id='n28' name='n28' href='#n28'>28</a>
<a class='no' id='n29' name='n29' href='#n29'>29</a>
<a class='no' id='n30' name='n30' href='#n30'>30</a>
<a class='no' id='n31' name='n31' href='#n31'>31</a>
<a class='no' id='n32' name='n32' href='#n32'>32</a>
<a class='no' id='n33' name='n33' href='#n33'>33</a>
<a class='no' id='n34' name='n34' href='#n34'>34</a>
<a class='no' id='n35' name='n35' href='#n35'>35</a>
<a class='no' id='n36' name='n36' href='#n36'>36</a>
<a class='no' id='n37' name='n37' href='#n37'>37</a>
<a class='no' id='n38' name='n38' href='#n38'>38</a>
<a class='no' id='n39' name='n39' href='#n39'>39</a>
<a class='no' id='n40' name='n40' href='#n40'>40</a>
<a class='no' id='n41' name='n41' href='#n41'>41</a>
<a class='no' id='n42' name='n42' href='#n42'>42</a>
<a class='no' id='n43' name='n43' href='#n43'>43</a>
<a class='no' id='n44' name='n44' href='#n44'>44</a>
<a class='no' id='n45' name='n45' href='#n45'>45</a>
<a class='no' id='n46' name='n46' href='#n46'>46</a>
<a class='no' id='n47' name='n47' href='#n47'>47</a>
<a class='no' id='n48' name='n48' href='#n48'>48</a>
<a class='no' id='n49' name='n49' href='#n49'>49</a>
<a class='no' id='n50' name='n50' href='#n50'>50</a>
<a class='no' id='n51' name='n51' href='#n51'>51</a>
<a class='no' id='n52' name='n52' href='#n52'>52</a>
<a class='no' id='n53' name='n53' href='#n53'>53</a>
<a class='no' id='n54' name='n54' href='#n54'>54</a>
<a class='no' id='n55' name='n55' href='#n55'>55</a>
<a class='no' id='n56' name='n56' href='#n56'>56</a>
<a class='no' id='n57' name='n57' href='#n57'>57</a>
<a class='no' id='n58' name='n58' href='#n58'>58</a>
<a class='no' id='n59' name='n59' href='#n59'>59</a>
<a class='no' id='n60' name='n60' href='#n60'>60</a>
<a class='no' id='n61' name='n61' href='#n61'>61</a>
<a class='no' id='n62' name='n62' href='#n62'>62</a>
<a class='no' id='n63' name='n63' href='#n63'>63</a>
<a class='no' id='n64' name='n64' href='#n64'>64</a>
<a class='no' id='n65' name='n65' href='#n65'>65</a>
<a class='no' id='n66' name='n66' href='#n66'>66</a>
<a class='no' id='n67' name='n67' href='#n67'>67</a>
<a class='no' id='n68' name='n68' href='#n68'>68</a>
<a class='no' id='n69' name='n69' href='#n69'>69</a>
<a class='no' id='n70' name='n70' href='#n70'>70</a>
<a class='no' id='n71' name='n71' href='#n71'>71</a>
<a class='no' id='n72' name='n72' href='#n72'>72</a>
<a class='no' id='n73' name='n73' href='#n73'>73</a>
<a class='no' id='n74' name='n74' href='#n74'>74</a>
<a class='no' id='n75' name='n75' href='#n75'>75</a>
<a class='no' id='n76' name='n76' href='#n76'>76</a>
<a class='no' id='n77' name='n77' href='#n77'>77</a>
<a class='no' id='n78' name='n78' href='#n78'>78</a>
<a class='no' id='n79' name='n79' href='#n79'>79</a>
<a class='no' id='n80' name='n80' href='#n80'>80</a>
<a class='no' id='n81' name='n81' href='#n81'>81</a>
<a class='no' id='n82' name='n82' href='#n82'>82</a>
<a class='no' id='n83' name='n83' href='#n83'>83</a>
<a class='no' id='n84' name='n84' href='#n84'>84</a>
<a class='no' id='n85' name='n85' href='#n85'>85</a>
<a class='no' id='n86' name='n86' href='#n86'>86</a>
<a class='no' id='n87' name='n87' href='#n87'>87</a>
<a class='no' id='n88' name='n88' href='#n88'>88</a>
<a class='no' id='n89' name='n89' href='#n89'>89</a>
<a class='no' id='n90' name='n90' href='#n90'>90</a>
<a class='no' id='n91' name='n91' href='#n91'>91</a>
<a class='no' id='n92' name='n92' href='#n92'>92</a>
<a class='no' id='n93' name='n93' href='#n93'>93</a>
<a class='no' id='n94' name='n94' href='#n94'>94</a>
<a class='no' id='n95' name='n95' href='#n95'>95</a>
<a class='no' id='n96' name='n96' href='#n96'>96</a>
<a class='no' id='n97' name='n97' href='#n97'>97</a>
<a class='no' id='n98' name='n98' href='#n98'>98</a>
<a class='no' id='n99' name='n99' href='#n99'>99</a>
<a class='no' id='n100' name='n100' href='#n100'>100</a>
<a class='no' id='n101' name='n101' href='#n101'>101</a>
<a class='no' id='n102' name='n102' href='#n102'>102</a>
<a class='no' id='n103' name='n103' href='#n103'>103</a>
<a class='no' id='n104' name='n104' href='#n104'>104</a>
<a class='no' id='n105' name='n105' href='#n105'>105</a>
<a class='no' id='n106' name='n106' href='#n106'>106</a>
<a class='no' id='n107' name='n107' href='#n107'>107</a>
<a class='no' id='n108' name='n108' href='#n108'>108</a>
<a class='no' id='n109' name='n109' href='#n109'>109</a>
<a class='no' id='n110' name='n110' href='#n110'>110</a>
<a class='no' id='n111' name='n111' href='#n111'>111</a>
<a class='no' id='n112' name='n112' href='#n112'>112</a>
<a class='no' id='n113' name='n113' href='#n113'>113</a>
<a class='no' id='n114' name='n114' href='#n114'>114</a>
<a class='no' id='n115' name='n115' href='#n115'>115</a>
<a class='no' id='n116' name='n116' href='#n116'>116</a>
</pre></td>
<td class='lines'><pre><code><span class="hl kwa">from</span> astrometry<span class="hl opt">.</span>util<span class="hl opt">.</span>pyfits_utils <span class="hl kwa">import</span> <span class="hl opt">*</span>
<span class="hl kwa">from</span> numpy <span class="hl kwa">import</span> <span class="hl opt">*</span>

<span class="hl kwa">def</span> <span class="hl kwd">mag2flux</span><span class="hl opt">(</span>mag<span class="hl opt">):</span>
    <span class="hl kwa">return</span> <span class="hl num">2.5</span><span class="hl opt">**-</span>mag

<span class="hl kwa">def</span> <span class="hl kwd">flux2mag</span><span class="hl opt">(</span>flux<span class="hl opt">):</span>
    <span class="hl kwa">return</span> <span class="hl opt">-</span><span class="hl kwd">log</span><span class="hl opt">(</span>flux<span class="hl opt">)/</span><span class="hl kwd">log</span><span class="hl opt">(</span><span class="hl num">2.5</span><span class="hl opt">)</span>

<span class="hl kwa">if</span> __name__ <span class="hl opt">==</span> <span class="hl str">'__main__'</span><span class="hl opt">:</span>
    T <span class="hl opt">=</span> <span class="hl kwd">fits_table</span><span class="hl opt">(</span><span class="hl str">'both3.fits'</span><span class="hl opt">)</span>
    <span class="hl kwa">print</span> <span class="hl str">'Got %i sources'</span> <span class="hl opt">%</span> <span class="hl kwb">len</span><span class="hl opt">(</span>T<span class="hl opt">)</span>

    ids <span class="hl opt">=</span> T<span class="hl opt">.</span><span class="hl kwb">id</span>
    U <span class="hl opt">=</span> <span class="hl kwd">unique</span><span class="hl opt">(</span>ids<span class="hl opt">)</span>
    <span class="hl kwa">print</span> <span class="hl str">'%i unique IDs'</span> <span class="hl opt">%</span> <span class="hl kwb">len</span><span class="hl opt">(</span>U<span class="hl opt">)</span>

    <span class="hl slc">#Assertion not valid since star and galaxy ids overlap.  The isGalaxy flag</span>
    <span class="hl slc">#breaks this degeneracy</span>
    <span class="hl slc">#assert(len(U) == len(T))</span>

    <span class="hl slc"># Secret decoder ring says ignore brighter than 10.</span>
    M <span class="hl opt">=</span> <span class="hl num">10</span>
    keep <span class="hl opt">= (</span>T<span class="hl opt">.</span>u <span class="hl opt">&gt;</span> M<span class="hl opt">) * (</span>T<span class="hl opt">.</span>g <span class="hl opt">&gt;</span> M<span class="hl opt">) * (</span>T<span class="hl opt">.</span>r <span class="hl opt">&gt;</span> M<span class="hl opt">) * (</span>T<span class="hl opt">.</span>i <span class="hl opt">&gt;</span> M<span class="hl opt">) * (</span>T<span class="hl opt">.</span>z <span class="hl opt">&gt;</span> M<span class="hl opt">) * (</span>T<span class="hl opt">.</span>y <span class="hl opt">&gt;</span> M<span class="hl opt">)</span>

    <span class="hl kwa">if False</span><span class="hl opt">:</span>
        <span class="hl slc"># Find limiting mags and cut 1 mag fainter.</span>
	step <span class="hl opt">=</span> <span class="hl num">0.1</span>
	lmag <span class="hl opt">= []</span>
	<span class="hl kwa">for</span> band <span class="hl kwa">in</span> <span class="hl str">'ugrizy'</span><span class="hl opt">:</span>
		mag <span class="hl opt">=</span> T<span class="hl opt">.</span><span class="hl kwd">get</span><span class="hl opt">(</span>band<span class="hl opt">)</span>
		bins <span class="hl opt">=</span> <span class="hl kwd">arange</span><span class="hl opt">(</span><span class="hl kwd">floor</span><span class="hl opt">(</span>mag<span class="hl opt">.</span><span class="hl kwb">min</span><span class="hl opt">() /</span> step<span class="hl opt">) *</span> step<span class="hl opt">,</span> <span class="hl kwd">ceil</span><span class="hl opt">(</span>mag<span class="hl opt">.</span><span class="hl kwb">max</span><span class="hl opt">() /</span> step<span class="hl opt">) *</span> step <span class="hl opt">+</span> step<span class="hl opt">,</span> step<span class="hl opt">)</span>
		n<span class="hl opt">,</span>b <span class="hl opt">=</span> <span class="hl kwd">histogram</span><span class="hl opt">(</span>mag<span class="hl opt">,</span> bins<span class="hl opt">=</span>bins<span class="hl opt">)</span>
		I <span class="hl opt">=</span> <span class="hl kwd">argmax</span><span class="hl opt">(</span>n<span class="hl opt">)</span>
		lmag<span class="hl opt">.</span><span class="hl kwd">append</span><span class="hl opt">(</span>b<span class="hl opt">[</span>I<span class="hl opt">])</span>
	bright <span class="hl opt">=</span> <span class="hl kwd">zeros_like</span><span class="hl opt">(</span>keep<span class="hl opt">)</span>
	<span class="hl kwa">for</span> i<span class="hl opt">,</span>band <span class="hl kwa">in</span> <span class="hl kwb">enumerate</span><span class="hl opt">(</span><span class="hl str">'ugrizy'</span><span class="hl opt">):</span>
		mag <span class="hl opt">=</span> T<span class="hl opt">.</span><span class="hl kwd">get</span><span class="hl opt">(</span>band<span class="hl opt">)</span>
		bright <span class="hl opt">=</span> <span class="hl kwd">logical_or</span><span class="hl opt">(</span>bright<span class="hl opt">,</span> mag <span class="hl opt">&lt; (</span>lmag<span class="hl opt">[</span>i<span class="hl opt">] +</span> <span class="hl num">1</span><span class="hl opt">))</span>
	keep <span class="hl opt">*=</span> bright

    <span class="hl kwa">else</span><span class="hl opt">:</span>
	<span class="hl slc"># Cut at any band brighter than ...</span>
	<span class="hl slc">#cut = 22.</span>
        <span class="hl str">''''</span>
<span class="hl str">        Got 12235294 sources</span>
<span class="hl str">        Band u : keeping 6009584 above mag 23.4</span>
<span class="hl str">        8 millionth mag: 24.313249588</span>
<span class="hl str">        Band g : keeping 7228012 above mag 22.4</span>
<span class="hl str">        8 millionth mag: 22.8702201843</span>
<span class="hl str">        Band r : keeping 7964639 above mag 22</span>
<span class="hl str">        8 millionth mag: 22.0967559814</span>
<span class="hl str">        Band i : keeping 7813477 above mag 21.7</span>
<span class="hl str">        8 millionth mag: 21.7739124298</span>
<span class="hl str">        Band z : keeping 7634632 above mag 21.5</span>
<span class="hl str">        8 millionth mag: 21.6284103394</span>
<span class="hl str">        Band y : keeping 7682476 above mag 21.4</span>
<span class="hl str">        8 millionth mag: 21.5253562927</span>
<span class="hl str">        After mag cuts: 8198432 sources</span>
<span class="hl str">        '''</span>
        cuts <span class="hl opt">= [</span> <span class="hl num">24.3</span><span class="hl opt">,</span> <span class="hl num">22.9</span><span class="hl opt">,</span> <span class="hl num">22.0</span><span class="hl opt">,</span> <span class="hl num">21.8</span><span class="hl opt">,</span> <span class="hl num">21.6</span><span class="hl opt">,</span> <span class="hl num">21.5</span> <span class="hl opt">]</span>

	magkeep <span class="hl opt">=</span> <span class="hl kwd">zeros_like</span><span class="hl opt">(</span>keep<span class="hl opt">)</span>
	<span class="hl kwa">for</span> band<span class="hl opt">,</span>cut <span class="hl kwa">in</span> <span class="hl kwb">zip</span><span class="hl opt">(</span><span class="hl str">'ugrizy'</span><span class="hl opt">,</span> cuts<span class="hl opt">):</span>
		mag <span class="hl opt">=</span> T<span class="hl opt">.</span><span class="hl kwd">get</span><span class="hl opt">(</span>band<span class="hl opt">)</span>
		I <span class="hl opt">= (</span>mag <span class="hl opt">&lt;</span> cut<span class="hl opt">)</span>
		<span class="hl kwa">print</span> <span class="hl str">'Band'</span><span class="hl opt">,</span> band<span class="hl opt">,</span> <span class="hl str">': keeping %i above mag %g'</span> <span class="hl opt">% (</span><span class="hl kwb">sum</span><span class="hl opt">(</span>I<span class="hl opt">),</span> cut<span class="hl opt">)</span>

                <span class="hl slc">#J = argsort(mag)</span>
                <span class="hl slc">#print '8 millionth mag:', mag[J[8000000]]</span>

		magkeep<span class="hl opt">[</span>I<span class="hl opt">] =</span> <span class="hl kwa">True</span>
	keep <span class="hl opt">*=</span> magkeep

	lmag <span class="hl opt">=</span> <span class="hl kwd">ones</span><span class="hl opt">(</span><span class="hl num">6</span><span class="hl opt">) *</span> cut

    T <span class="hl opt">=</span> T<span class="hl opt">[</span>keep<span class="hl opt">]</span>
    <span class="hl kwa">print</span> <span class="hl str">'After mag cuts: %i sources'</span> <span class="hl opt">%</span> <span class="hl kwb">len</span><span class="hl opt">(</span>T<span class="hl opt">)</span>

    <span class="hl kwa">for</span> i<span class="hl opt">,</span>band <span class="hl kwa">in</span> <span class="hl kwb">enumerate</span><span class="hl opt">(</span><span class="hl str">'ugrizy'</span><span class="hl opt">):</span>
	mag <span class="hl opt">=</span> T<span class="hl opt">.</span><span class="hl kwd">get</span><span class="hl opt">(</span>band<span class="hl opt">)</span>
	<span class="hl slc"># Invent magnitude errors</span>
	flux0 <span class="hl opt">=</span> <span class="hl kwd">mag2flux</span><span class="hl opt">(</span>lmag<span class="hl opt">[</span>i<span class="hl opt">])</span>
	<span class="hl slc"># assume that's 5-sigma;</span>
	nsigma <span class="hl opt">=</span> <span class="hl num">5</span><span class="hl opt">.</span>
	<span class="hl slc"># assume sky counts / pixel</span>
	sky <span class="hl opt">=</span> <span class="hl num">100</span><span class="hl opt">.</span>
	fluxscale <span class="hl opt">=</span> <span class="hl kwd">sqrt</span><span class="hl opt">(</span>sky<span class="hl opt">) / (</span>flux0 <span class="hl opt">/</span> nsigma<span class="hl opt">)</span>

	<span class="hl slc"># assumed minimum magnitude error level.</span>
	noisefloor <span class="hl opt">=</span> <span class="hl num">0.01</span>

	flux <span class="hl opt">=</span> fluxscale <span class="hl opt">*</span> <span class="hl kwd">mag2flux</span><span class="hl opt">(</span>mag<span class="hl opt">)</span>
	<span class="hl slc">#magerr = flux2mag(sqrt(flux  +	 sky) / flux)</span>
	magerr <span class="hl opt">=</span> <span class="hl kwd">hypot</span><span class="hl opt">(</span>noisefloor<span class="hl opt">,</span> <span class="hl kwd">flux2mag</span><span class="hl opt">(</span><span class="hl num">1</span><span class="hl opt">. +</span> <span class="hl kwd">sqrt</span><span class="hl opt">(</span>flux  <span class="hl opt">+</span>  sky<span class="hl opt">) /</span> flux<span class="hl opt">))</span>

	T<span class="hl opt">.</span><span class="hl kwb">set</span><span class="hl opt">(</span>band <span class="hl opt">+</span> <span class="hl str">'_err'</span><span class="hl opt">,</span> magerr<span class="hl opt">)</span>

    <span class="hl slc"># Seems I messed this up!</span>

    <span class="hl kwa">print</span> <span class="hl str">'variable:'</span><span class="hl opt">,</span> T<span class="hl opt">.</span>variable<span class="hl opt">.</span>shape
    <span class="hl kwa">print</span> <span class="hl str">'variable:'</span><span class="hl opt">,</span> <span class="hl kwd">unique</span><span class="hl opt">(</span>T<span class="hl opt">.</span>variable<span class="hl opt">)</span>

    T<span class="hl opt">.</span>starnotgal <span class="hl opt">=</span> T<span class="hl opt">.</span>starnotgal<span class="hl opt">[:,</span><span class="hl num">0</span><span class="hl opt">]</span>
    T<span class="hl opt">.</span>variable <span class="hl opt">=</span> T<span class="hl opt">.</span>variable<span class="hl opt">[:,</span><span class="hl num">0</span><span class="hl opt">]</span>

    <span class="hl slc"># down-convert</span>
    <span class="hl kwa">for</span> band <span class="hl kwa">in</span> <span class="hl str">'ugrizy'</span><span class="hl opt">:</span>
	T<span class="hl opt">.</span><span class="hl kwb">set</span><span class="hl opt">(</span>band<span class="hl opt">,</span> T<span class="hl opt">.</span><span class="hl kwd">get</span><span class="hl opt">(</span>band<span class="hl opt">).</span><span class="hl kwd">astype</span><span class="hl opt">(</span>float32<span class="hl opt">))</span>
	T<span class="hl opt">.</span><span class="hl kwb">set</span><span class="hl opt">(</span>band <span class="hl opt">+</span> <span class="hl str">'_err'</span><span class="hl opt">,</span> T<span class="hl opt">.</span><span class="hl kwd">get</span><span class="hl opt">(</span>band <span class="hl opt">+</span> <span class="hl str">'_err'</span><span class="hl opt">).</span><span class="hl kwd">astype</span><span class="hl opt">(</span>float32<span class="hl opt">))</span>
    <span class="hl kwa">for</span> c <span class="hl kwa">in</span> <span class="hl opt">[</span><span class="hl str">'mura'</span><span class="hl opt">,</span><span class="hl str">'mudec'</span><span class="hl opt">,</span><span class="hl str">'parallax'</span><span class="hl opt">]:</span>
	T<span class="hl opt">.</span><span class="hl kwb">set</span><span class="hl opt">(</span>c<span class="hl opt">,</span> T<span class="hl opt">.</span><span class="hl kwd">get</span><span class="hl opt">(</span>c<span class="hl opt">).</span><span class="hl kwd">astype</span><span class="hl opt">(</span>float32<span class="hl opt">))</span>

    T<span class="hl opt">.</span><span class="hl kwd">about</span><span class="hl opt">()</span>

    T<span class="hl opt">.</span><span class="hl kwd">writeto</span><span class="hl opt">(</span><span class="hl str">'both4.fits'</span><span class="hl opt">)</span>
</code></pre></td></tr></table>
</div> <!-- class=content -->
<div class='footer'>generated  by cgit v0.9.0.2-39-g756e at 2012-07-17 12:08:32 (GMT)</div>
</div> <!-- id=cgit -->
</body>
</html>
