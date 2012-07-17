<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>
<head>
<title>contrib/demos/lsst_dm_stack_demo.git - DM stack demos for end users
</title>
<meta name='generator' content='cgit v0.9.0.2-39-g756e'/>
<meta name='robots' content='index, nofollow'/>
<link rel='stylesheet' type='text/css' href='/cgit.static/cgit.css'/>
<link rel='alternate' title='Atom feed' href='http://dev.lsstcorp.org/cgit/contrib/demos/lsst_dm_stack_demo.git/atom/bin/demo.sh?h=master' type='application/atom+xml'/>
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
<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/'>summary</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/refs/'>refs</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/log/bin/demo.sh'>log</a><a class='active' href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/bin/demo.sh'>tree</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/commit/bin/demo.sh'>commit</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/diff/bin/demo.sh'>diff</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/stats/bin/demo.sh'>stats</a></td><td class='form'><form class='right' method='get' action='/cgit/contrib/demos/lsst_dm_stack_demo.git/log/bin/demo.sh'>
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
<div class='path'>path: <a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/'>root</a>/<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/bin'>bin</a>/<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/bin/demo.sh'>demo.sh</a></div><div class='content'>blob: 16f6e2dae546f72d22dd0459066505e50559d0d6 (<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/plain/bin/demo.sh'>plain</a>)
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
</pre></td>
<td class='lines'><pre><code><span class="hl slc">#!/bin/bash</span>

<span class="hl kwb">type</span> processCcdLsstSim.py <span class="hl opt">&gt;/</span>dev<span class="hl opt">/</span>null <span class="hl num">2</span><span class="hl opt">&gt;&amp;</span><span class="hl num">1</span> || <span class="hl opt">{</span> <span class="hl kwb">echo</span> <span class="hl str">&quot;Could not find processCcdLsstSim.py on your path. Have you sourced loadLSST.sh, and setup-ed pipe_tasks?&quot;</span><span class="hl opt">;</span> <span class="hl kwb">exit</span> <span class="hl num">1</span><span class="hl opt">; }</span>
<span class="hl kwb">test</span> <span class="hl opt">-</span>d input || <span class="hl opt">{</span> <span class="hl kwb">echo</span> <span class="hl str">&quot;Could not fine the 'input' directory. Run this script from the directory where the 'input' subdirectory resides.&quot;</span><span class="hl opt">;</span> <span class="hl kwb">exit</span> <span class="hl num">1</span><span class="hl opt">; }</span>
<span class="hl kwb">test</span> <span class="hl opt">-</span>d astrometry_net_data || <span class="hl opt">{</span> <span class="hl kwb">echo</span> <span class="hl str">&quot;Could not fine the 'astrometry_net_data' directory.&quot;</span><span class="hl opt">;</span> <span class="hl kwb">exit</span> <span class="hl num">1</span><span class="hl opt">; }</span>
<span class="hl kwb">test</span> <span class="hl str">&quot;$(type -t setup)&quot;</span> <span class="hl opt">==</span> <span class="hl str">&quot;function&quot;</span> || <span class="hl opt">{</span> <span class="hl kwb">export</span> SHELL<span class="hl opt">=/</span>bin<span class="hl opt">/</span>bash<span class="hl opt">;</span> <span class="hl kwb">source</span> <span class="hl kwd">$LSST_HOME</span><span class="hl opt">/</span>eups<span class="hl opt">/</span>default<span class="hl opt">/</span>bin<span class="hl opt">/</span>setups.sh<span class="hl opt">; }</span> <span class="hl slc"># Ensure 'setup' alias is defined (may happen if the user is not running bash)</span>
<span class="hl kwb">set</span> <span class="hl opt">-</span>e

<span class="hl slc"># Tell the stack where to find astrometric reference catalogs</span>
setup <span class="hl opt">--</span>nolocks <span class="hl opt">-</span>v <span class="hl opt">-</span>r .<span class="hl opt">/</span>astrometry_net_data astrometry_net_data

<span class="hl kwc">rm</span> <span class="hl opt">-</span>rf output detected<span class="hl opt">-</span>sources.txt
processCcdLsstSim.py lsstSim input <span class="hl opt">--</span>id visit<span class="hl opt">=</span><span class="hl num">88689461</span> raft<span class="hl opt">=</span><span class="hl num">2</span><span class="hl opt">,</span><span class="hl num">3</span> sensor<span class="hl opt">=</span><span class="hl num">1</span><span class="hl opt">,</span><span class="hl num">1</span> <span class="hl opt">--</span>out output
.<span class="hl opt">/</span>bin<span class="hl opt">/</span><span class="hl kwb">export</span><span class="hl opt">-</span>results output <span class="hl opt">&gt;</span> detected<span class="hl opt">-</span>sources.txt

<span class="hl kwb">echo</span>
<span class="hl kwb">echo</span> <span class="hl str">&quot;Processing completed successfully. The results are in detected-sources.txt.&quot;</span>
</code></pre></td></tr></table>
</div> <!-- class=content -->
<div class='footer'>generated  by cgit v0.9.0.2-39-g756e at 2012-07-17 12:09:53 (GMT)</div>
</div> <!-- id=cgit -->
</body>
</html>
