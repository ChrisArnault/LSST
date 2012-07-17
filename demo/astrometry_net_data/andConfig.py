<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>
<head>
<title>contrib/demos/lsst_dm_stack_demo.git - DM stack demos for end users
</title>
<meta name='generator' content='cgit v0.9.0.2-39-g756e'/>
<meta name='robots' content='index, nofollow'/>
<link rel='stylesheet' type='text/css' href='/cgit.static/cgit.css'/>
<link rel='alternate' title='Atom feed' href='http://dev.lsstcorp.org/cgit/contrib/demos/lsst_dm_stack_demo.git/atom/astrometry_net_data/andConfig.py?h=master' type='application/atom+xml'/>
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
<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/'>summary</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/refs/'>refs</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/log/astrometry_net_data/andConfig.py'>log</a><a class='active' href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/astrometry_net_data/andConfig.py'>tree</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/commit/astrometry_net_data/andConfig.py'>commit</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/diff/astrometry_net_data/andConfig.py'>diff</a><a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/stats/astrometry_net_data/andConfig.py'>stats</a></td><td class='form'><form class='right' method='get' action='/cgit/contrib/demos/lsst_dm_stack_demo.git/log/astrometry_net_data/andConfig.py'>
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
<div class='path'>path: <a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/'>root</a>/<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/astrometry_net_data'>astrometry_net_data</a>/<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/tree/astrometry_net_data/andConfig.py'>andConfig.py</a></div><div class='content'>blob: 511f5b0ba054bc01f378d6289306573d2ccccb60 (<a href='/cgit/contrib/demos/lsst_dm_stack_demo.git/plain/astrometry_net_data/andConfig.py'>plain</a>)
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
</pre></td>
<td class='lines'><pre><code>root<span class="hl opt">.</span>starGalaxyColumn <span class="hl opt">=</span> <span class="hl str">&quot;starnotgal&quot;</span>
filters <span class="hl opt">= (</span><span class="hl str">'u'</span><span class="hl opt">,</span> <span class="hl str">'g'</span><span class="hl opt">,</span> <span class="hl str">'r'</span><span class="hl opt">,</span> <span class="hl str">'i'</span><span class="hl opt">,</span> <span class="hl str">'z'</span><span class="hl opt">,</span> <span class="hl str">'y'</span><span class="hl opt">)</span>
root<span class="hl opt">.</span>magColumnMap <span class="hl opt">=</span> <span class="hl kwb">dict</span><span class="hl opt">([(</span>f<span class="hl opt">,</span>f<span class="hl opt">)</span> <span class="hl kwa">for</span> f <span class="hl kwa">in</span> filters<span class="hl opt">])</span>
root<span class="hl opt">.</span>magErrorColumnMap <span class="hl opt">=</span> <span class="hl kwb">dict</span><span class="hl opt">([(</span>f<span class="hl opt">,</span> f <span class="hl opt">+</span> <span class="hl str">'_err'</span><span class="hl opt">)</span> <span class="hl kwa">for</span> f <span class="hl kwa">in</span> filters<span class="hl opt">])</span>
root<span class="hl opt">.</span>indexFiles <span class="hl opt">= [</span><span class="hl str">'index-120319000.fits'</span><span class="hl opt">,</span>
                   <span class="hl str">'index-120319001.fits'</span><span class="hl opt">,</span>
                   <span class="hl str">'index-120319002.fits'</span><span class="hl opt">,</span>
                   <span class="hl str">'index-120319003.fits'</span><span class="hl opt">,</span>
                   <span class="hl opt">]</span>

</code></pre></td></tr></table>
</div> <!-- class=content -->
<div class='footer'>generated  by cgit v0.9.0.2-39-g756e at 2012-07-17 12:06:11 (GMT)</div>
</div> <!-- id=cgit -->
</body>
</html>