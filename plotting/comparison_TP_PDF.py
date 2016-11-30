#import numpy
import os
from ROOT import *
from array import array

Data={}

Data['TrackJets']={
      'TP0':{
              '60':{
                        'sys':[0.074,0.025,0.018,0.018,0.025],
                       'stat':[0.019,0.012,0.006,0.008,0.016],
                      'total':[0.077,0.028,0.019,0.020,0.030],
                         'sf':[1.061,1.048,1.023,1.020,0.987],
              },
              '70':{
                        'sys':[0.070,0.026,0.016,0.014,0.020],
                       'stat':[0.014,0.009,0.005,0.007,0.012],
                      'total':[0.072,0.028,0.017,0.015,0.023],
                         'sf':[1.038,1.029,1.016,1.018,0.985],
              },
              '77':{
                        'sys':[0.057,0.030,0.016,0.012,0.024],
                       'stat':[0.011,0.008,0.004,0.006,0.011],
                      'total':[0.058,0.031,0.017,0.013,0.026],
                         'sf':[1.023,1.029,1.014,1.012,0.981],
              },
              '85':{
                        'sys':[0.061,0.027,0.012,0.010,0.016],
                       'stat':[0.009,0.006,0.003,0.004,0.009],
                      'total':[0.061,0.028,0.013,0.011,0.018],
                         'sf':[1.029,1.023,1.015,1.013,0.995],
              },
      },

      'TP1':{
              '60':{
                        'sys':[0.034,0.025,0.024,0.022,0.062],
                       'stat':[0.011,0.009,0.005,0.007,0.013],
                      'total':[0.035,0.027,0.025,0.024,0.064],
                         'sf':[1.035,1.011,0.988,0.989,0.960],
              },
              '70':{
                        'sys':[0.036,0.025,0.024,0.022,0.059],
                       'stat':[0.008,0.007,0.004,0.006,0.012],
                      'total':[0.037,0.026,0.025,0.023,0.061],
                         'sf':[1.030,1.007,0.986,0.988,0.957],
              },
              '77':{
                        'sys':[0.036,0.024,0.025,0.022,0.058],
                       'stat':[0.007,0.006,0.004,0.005,0.011],
                      'total':[0.037,0.025,0.025,0.022,0.059],
                         'sf':[1.026,1.014,0.994,0.994,0.956],
              },
              '85':{
                        'sys':[0.035,0.024,0.025,0.020,0.059],
                       'stat':[0.006,0.005,0.003,0.005,0.010],
                      'total':[0.036,0.024,0.025,0.021,0.060],
                         'sf':[1.040,1.026,1.006,0.996,0.966],
              },
      },

      'PDF':{
              '60':{
                        'sys':[0.072,0.033,0.020,0.027,0.056,0.108],
                       'stat':[0.012,0.008,0.007,0.006,0.011,0.092],
                      'total':[0.073,0.034,0.022,0.028,0.057,0.142],
                         'sf':[1.067,1.054,1.027,1.006,0.971,0.747],
              },
              '70':{
                        'sys':[0.080,0.029,0.017,0.023,0.051,0.102],
                       'stat':[0.009,0.005,0.004,0.004,0.009,0.085],
                      'total':[0.081,0.029,0.017,0.023,0.052,0.133],
                         'sf':[1.043,1.041,1.023,1.004,0.969,0.784],
              },
              '77':{
                        'sys':[0.067,0.027,0.016,0.021,0.048,0.093],
                       'stat':[0.006,0.004,0.003,0.004,0.009,0.077],
                      'total':[0.067,0.027,0.016,0.021,0.049,0.121],
                         'sf':[1.046,1.042,1.022,1.006,0.970,0.719],
              },
              '85':{
                        'sys':[0.068,0.026,0.016,0.018,0.047,0.104],
                       'stat':[0.007,0.004,0.002,0.004,0.008,0.050],
                      'total':[0.068,0.027,0.017,0.018,0.048,0.116],
                         'sf':[1.040,1.036,1.021,1.007,0.981,0.959],
              },
      }
}

Data['Calo Jets']={
      'TP0':{
              '60':{
                        'sys':[0.087,0.029,0.017,0.021,0.035,0.050],
                       'stat':[0.034,0.008,0.007,0.009,0.018,0.038],
                      'total':[0.093,0.029,0.018,0.023,0.039,0.063],
                         'sf':[1.089,1.030,1.023,1.027,1.008,1.020],
              },
              '70':{
                        'sys':[0.084,0.030,0.015,0.015,0.032,0.049],
                       'stat':[0.026,0.006,0.006,0.007,0.014,0.028],
                      'total':[0.088,0.030,0.016,0.016,0.035,0.056],
                         'sf':[1.063,1.021,1.025,1.025,1.002,1.016],
              },
              '77':{
                        'sys':[0.083,0.026,0.015,0.014,0.025,0.036],
                       'stat':[0.022,0.005,0.005,0.005,0.011,0.023],
                      'total':[0.085,0.026,0.016,0.015,0.027,0.043],
                         'sf':[1.067,1.024,1.017,1.021,1.007,1.009],
              },
              '85':{
                        'sys':[0.077,0.024,0.012,0.013,0.020,0.031],
                       'stat':[0.018,0.004,0.004,0.004,0.008,0.018],
                      'total':[0.079,0.025,0.013,0.014,0.022,0.036],
                         'sf':[1.073,1.022,1.018,1.012,1.002,0.988],
              },
      },

      'PDF':{
              '60':{
                        'sys':[0.124,0.032,0.018,0.023,0.027,0.039],
                       'stat':[0.015,0.004,0.005,0.005,0.012,0.023],
                      'total':[0.125,0.032,0.019,0.024,0.030,0.045],
                         'sf':[0.993,1.037,1.029,1.019,0.995,0.965],
              },
              '70':{
                        'sys':[0.118,0.030,0.018,0.022,0.026,0.035],
                       'stat':[0.014,0.004,0.004,0.004,0.010,0.019],
                      'total':[0.118,0.030,0.018,0.022,0.028,0.040],
                         'sf':[0.988,1.036,1.030,1.014,0.981,0.967],
              },
              '77':{
                        'sys':[0.117,0.028,0.017,0.021,0.023,0.034],
                       'stat':[0.012,0.004,0.004,0.003,0.010,0.016],
                      'total':[0.118,0.029,0.017,0.021,0.025,0.038],
                         'sf':[1.009,1.042,1.028,1.012,0.977,0.966],
              },
              '85':{
                        'sys':[0.121,0.028,0.015,0.018,0.021,0.031],
                       'stat':[0.009,0.003,0.003,0.003,0.008,0.013],
                      'total':[0.121,0.028,0.015,0.018,0.022,0.034],
                         'sf':[1.024,1.038,1.026,1.010,0.985,0.955],
              },
      }
}

# bin info
XAxis = {
   'Calo Jets':[ '20-30GeV', '30-60GeV', '60-90GeV', '90-140GeV', '140-200GeV', '200-300GeV' ],
   'TrackJets':[ '10-20GeV', '20-30GeV', '30-60GeV', '60-100GeV', '100-250GeV']#, '250-300' ],
}

ErrSet  = {
   'total':{'colo':-1,'pos':0, 'line':1},
     'sys':{'colo':-1,'pos':1, 'line':2},
    'stat':{'colo':-1,'pos':2, 'line':3},
}

# general setting
suffix  = 'eps'
lumi    = '27.65'
width   = 0.8
Central = {  'name':'sf',
          'OutName':'scalefactor',
	    'title':'scale factors',
	 'DrawLine':True,
	       'LP':[0.55,0.65,0.9,0.9],
	    'width':800,
	   'height':600,
       'LegColumns':1,
          'LabSize':0.1,
	  }

PlotTitle = 'Comparison between TP and PDF'

MethodSet = {
   'PDF':{'line':-1,'shift':0,'colo':kBlue},
   'TP0':{'line':-1,'shift':1,'colo':kBlack},
}

# plotting function
def ATLAS_LABEL(x, y, color):
   l=TLatex()
   l.SetNDC()
   l.SetTextFont(72)
   l.SetTextColor(color)
   l.DrawLatex(x,y,"ATLAS")

def myText(x, y, color, text):
   l=TLatex() #l.SetTextAlign(12); l.SetTextSize(tsize); 
   l.SetNDC()
   l.SetTextColor(color)
   l.DrawLatex(x,y,text)

def DrawLine(xmin,ypos,xmax,co):
   line = TLine(xmin, ypos, xmax, ypos)
   line.SetLineColor(co)
   line.SetLineStyle(2)
   line.SetLineWidth(3)
   return line

def MakePlot( Jet, WP, DataPool ):
    Title = '%s at %s WP of %s Calibration'%(PlotTitle,WP,Jet)
    c1 = TCanvas('c1',Title,Central['width'],Central['height']);
    mg = TMultiGraph("mg",Title);
    leg = TLegend( Central['LP'][0], Central['LP'][1], Central['LP'][2], Central['LP'][3] )
    leg.SetNColumns(Central['LegColumns'])
    #leg.SetTextFont(42)
    #leg.SetTextSize(0.04)
    leg.SetFillColor(0)
    leg.SetLineColor(0)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    for index in range(0,len(MethodSet)):
       for mt in MethodSet:
	  if index == MethodSet[mt]['shift']: break
       for pos in range(0,len(ErrSet)):
	  for err in ErrSet:
	     if pos == ErrSet[err]['pos'] : break
	  g,l=MakeGraph(mt, Jet, WP, err, DataPool)
	  mg.Add(g)
	  leg.AddEntry(g,l,"lp")
    NItems = len(XAxis[Jet])
    #mg.SetMinimum(0.)
    #mg.SetMaximum(NItems+1)
    mg.Draw('AP')
    xax = mg.GetXaxis()
    for ix in range(NItems):
       #print xax.FindBin(ix+1)
       xax.SetBinLabel(xax.FindBin(ix+1),XAxis[Jet][ix])
    xax.LabelsOption("h")
    xax.SetLabelSize(Central['LabSize'])
    leg.Draw()

    # draw line one
    c1.Update()
    L_One = TLine(c1.GetUxmin(), 1., c1.GetUxmax(), 1.);
    L_One.SetLineColor(kGreen)
    L_One.SetLineStyle(2)
    L_One.SetLineWidth(3)
    if Central['DrawLine']: L_One.Draw()

    mg.GetYaxis().SetRangeUser(c1.GetUymin(), c1.GetUymin()+1.25*(c1.GetUymax()-c1.GetUymin()) );
    ATLAS_LABEL(0.12, 0.85, 1)

    l_LS=TLatex()
    l_LS.SetNDC()
    l_LS.SetTextSize(0.04)
    l_LS.SetTextColor(1)
    l_LS.DrawLatex(0.12, 0.78, "#intLdt = %s fb^{-1}   #sqrt{s} = 13 TeV"%lumi)
    myText(0.25, 0.85, 1, 'Internal')

    # make a color test
    #mg.GetYaxis().SetRangeUser( -1.0, 20.0 );
    #lines = []
    #ypos = 1.0
    #for co in [100, 96, 91, 88, 84, 71, 67, 62, 60, 55, 53, 51]:
    #for co in [100, 96, 93, 91, 88, 84, 74, 70, 67, 65, 62, 51]:
    #   print 'color %d'%co
    #   ypos = 1+ypos
    #   line=DrawLine(c1.GetUxmin(),ypos,c1.GetUxmax(),co)
    #   lines.append(line)

    #for line in lines:
    #   line.Draw()

    if not os.path.isdir("./complots/"):
        os.mkdir('./complots/')
    c1.Print('./complots/Com_%s_%s_%s.%s'%(Jet.replace(' ',''),WP,Central['OutName'],suffix))
    del c1

def MakePlotSplit( Jet, WP, DataPool ):
    NItems = len(XAxis[Jet])
    for err in ErrSet:
       for ib in range( NItems ):
          Title = '%s at %s WP of %s Calibration of %s in %d ptbin'%(PlotTitle,WP,Jet,err,ib+1)
          c1 = TCanvas('c1',Title,Central['width'],Central['height']);
          mg = TMultiGraph("mg",Title);
          leg = TLegend( Central['LP'][0], Central['LP'][1], Central['LP'][2], Central['LP'][3] )
          leg.SetNColumns(Central['LegColumns'])
          #leg.SetTextFont(42)
          #leg.SetTextSize(0.04)
          leg.SetFillColor(0)
          leg.SetLineColor(0)
          leg.SetFillStyle(0)
          leg.SetBorderSize(0)
          for index in range(0,len(MethodSet)):
             for mt in MethodSet:
                if index == MethodSet[mt]['shift']: break
             g,l=MakeGraphSplit(mt, Jet, WP, err, DataPool,ib)
             mg.Add(g)
             leg.AddEntry(g,l,"p")
          mg.Draw('AP')
          leg.Draw()

          # draw line one
          c1.Update()
          L_One = TLine(c1.GetUxmin(), 1., c1.GetUxmax(), 1.);
          L_One.SetLineColor(kGreen)
          L_One.SetLineStyle(2)
          L_One.SetLineWidth(3)
          if Central['DrawLine']: L_One.Draw()
          mg.GetYaxis().SetRangeUser(c1.GetUymin(), c1.GetUymin()+1.25*(c1.GetUymax()-c1.GetUymin()) );
          ATLAS_LABEL(0.12, 0.85, 1)

          l_LS=TLatex()
          l_LS.SetNDC()
          l_LS.SetTextSize(0.04)
          l_LS.SetTextColor(1)
          l_LS.DrawLatex(0.12, 0.78, "#intLdt = %s fb^{-1}   #sqrt{s} = 13 TeV"%lumi)
          myText(0.25, 0.85, 1, 'Internal')

          if not os.path.isdir("./complots/"):
              os.mkdir('./complots/')
          c1.Print('./complots/Com_%s_%s_%s_%s_%d.%s'%(Jet.replace(' ',''),WP,Central['OutName'],err,ib+1,suffix))
          del c1

def MakeCentralWithErr( CR, bins, Err ): #Calibration Results
    #y = numpy.ndarray( [bins] )
    #ey= numpy.ndarray( [bins] )
    #ex= numpy.ndarray( [bins] )
    y = []
    ey=[]
    ex=[]
    for ib in range( bins ):
        #y[ib]  = CR[Central['name']][ib]
        #ex[ib] = 0.
        #ey[ib] = CR[Err][ib]
	if type(CR[Central['name']][ib]) is str:
	   y.append(float(CR[Central['name']][ib]))
	   ey.append(float(CR[Err][ib]))
	else:
           y.append(CR[Central['name']][ib])
           ey.append(CR[Err][ib])
        ex.append(0.)
	#print y[ib],ex[ib],ey[ib]
    array_y = array( 'd',y )
    array_ex= array( 'd',ex )
    array_ey= array( 'd',ey )
    return array_y,array_ex,array_ey

def MakeErr( CR, ptbin, Err ): #Calibration Results
    ey=[]
    if type(CR[Err][ptbin]) is str:
        ey.append(float(CR[Err][ptbin]))
    else:
        ey.append(CR[Err][ptbin])
    array_ey= array( 'd',ey )
    return array_ey

def MakeGraph( Method, Jet, WP, Err, DataPool):
    name = '%s with %s from %s at %s WP of %s'%(Central['title'],Err,Method,WP,Jet)
    lname= '%s with %5s from %s'%(Central['name'],Err,Method)
    NItems = len(XAxis[Jet])
    shift = MethodSet[Method]['shift']*width/(len(ErrSet)*(len(MethodSet)+1))
    binpos = 1.+shift-width/2.+ErrSet[Err]['pos']*width/len(ErrSet)
    #x = numpy.ndarray( [NItems] )
    x_pos = []
    for ib in range( NItems ):
       x_pos.append( ib + binpos )
       #print x[ib]
    x = array('d', x_pos)
    CR = DataPool[Jet][Method][WP]
    y, ex, ey = MakeCentralWithErr( CR, NItems, Err )
    #print x
    #print y
    #print ex
    #print ey
    g = TGraphErrors( NItems, x, y, ex, ey )
    g.SetLineWidth(1)

    if ErrSet[Err]['line'] > 0: g.SetLineStyle( ErrSet[Err]['line'] )
    if ErrSet[Err]['colo'] > 0: 
       g.SetLineColor( ErrSet[Err]['colo'] )
       g.SetMarkerColor(ErrSet[Err]['colo']);
    if MethodSet[Method]['line'] > 0: g.SetLineStyle( MethodSet[Method]['line'] )
    if MethodSet[Method]['colo'] > 0:
       g.SetLineColor( MethodSet[Method]['colo'] )
       g.SetMarkerColor(MethodSet[Method]['colo']);

    g.SetMarkerStyle(8);
    g.SetMarkerSize(1);
    g.SetTitle(name)
    return g,lname

def MakeGraphSplit( Method, Jet, WP, Err, DataPool, ptbin):
    name = '%s with %s from %s at %s WP of %s uncertainty'%(Central['title'],Err,Method,WP,Jet)
    #lname= '%s with %5s from %s'%(Central['name'],Err,Method)
    lname= '%s'%Method
    x = array('d', [1+MethodSet[Method]['shift']])
    CR = DataPool[Jet][Method][WP]
    ey = MakeErr( CR, ptbin, Err )
    g = TGraph( 1, x, ey )
    g.SetLineWidth(1)
    g.SetLineStyle(1)

    if ErrSet[Err]['colo'] > 0: 
       g.SetLineColor( ErrSet[Err]['colo'] )
       g.SetMarkerColor(ErrSet[Err]['colo']);
    if MethodSet[Method]['colo'] > 0:
       g.SetLineColor( MethodSet[Method]['colo'] )
       g.SetMarkerColor(MethodSet[Method]['colo']);

    g.SetMarkerStyle(8);
    g.SetMarkerSize(2);
    g.SetTitle(name)
    return g,lname

def ShowBreakDown( Method, Jet, WP, DataPool):
    CR = DataPool[Jet][Method][WP]
    print '%s at %s with %s of %s'%(Central['name'], WP, Method, Jet )
    # show scale factors
    print '%s '%Central['name'],
    for ib in range(len(XAxis[Jet])):
        print '%s '%CR[Central['name']][ib],
    print

    # show errors
    for pos in range(0,len(ErrSet)):
        for err in ErrSet:
	    if pos == ErrSet[err]['pos'] : break
	print '%s '%err,
        for ib in range(len(XAxis[Jet])):
	    print '%s '%CR[err][ib],
	print
    
gROOT.SetBatch(1)

if __name__=='__main__':
   #MakePlot('TrackJets','60',Data)
   #MakePlot('TrackJets','70',Data)
   #MakePlot('TrackJets','77',Data)
   #MakePlot('TrackJets','85',Data)
   
   #MakePlot('Calo Jets','60',Data)
   #MakePlot('Calo Jets','70',Data)
   #MakePlot('Calo Jets','77',Data)
   MakePlot('Calo Jets','85',Data)
   #MakePlotSplit( 'Calo Jets', '85', Data )

   # compare with Chloe Only Track Jets
   MethodSet['TP1']={'line':-1,'shift':2,'colo':kRed}
   MakePlot('TrackJets','60',Data)
   MakePlot('TrackJets','70',Data)
   MakePlot('TrackJets','77',Data)
   MakePlot('TrackJets','85',Data)
   ShowBreakDown( 'TP0', 'Calo Jets', '77', Data)
   ShowBreakDown( 'TP0', 'TrackJets', '77', Data)
