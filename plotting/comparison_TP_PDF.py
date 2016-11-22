import numpy
from ROOT import *

Data={}

Data['TrackJets']={
      'T_P':{
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
      'T_P':{
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
   'Calo Jets':[ '20-30', '30-60', '60-90', '90-140', '140-200', '200-300' ],
   'TrackJets':[ '10-20', '20-30', '30-60', '60-100', '100-250', '250-300' ],
}

ErrSet  = {
   'total':{'colo':kBlack,'pos':0, 'line':-1},
     'sys':{'colo':kBlue, 'pos':1, 'line':-1},
    'stat':{'colo':kRed,  'pos':2, 'line':-1},
}

# general setting
suffix  = 'eps'
lumi    = '27.65'
width   = 0.8
Central = {  'name':'sf',
	    'title':'scale factors',
	 'DrawLine':True,
	       'LP':[0.55,0.65,0.9,0.9],
	    'width':800,
	   'height':600,
	  }

PlotTitle = 'Comparison between TP and PDF'

MethodSet = {
   'T_P':{'line':1,'shift':0,'colo':-1},
   'PDF':{'line':2,'shift':1,'colo':-1},
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
    #leg.SetTextFont(42)
    #leg.SetTextSize(0.04)
    leg.SetFillColor(0)
    leg.SetLineColor(0)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    for mt in MethodSet:
       for err in ErrSet:
	  g,l=MakeGraph(mt, Jet, WP, err, DataPool)
	  mg.Add(g)
	  leg.AddEntry(g,l,"lp")
    NItems = len(XAxis[Jet])
    #mg.SetMinimum(0.)
    #mg.SetMaximum(NItems+1)
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

    c1.Print('./complots/Com_%s_%s_%s.%s'%(Jet.replace(' ',''),WP,Central['name'],suffix))
    del c1

def MakeCentralWithErr( CR, bins, Err ): #Calibration Results
    y = numpy.ndarray( [bins] )
    ey= numpy.ndarray( [bins] )
    ex= numpy.ndarray( [bins] )
    for ib in range( bins ):
        y[ib]  = CR[Central['name']][ib]
        ex[ib] = 0.
        ey[ib] = CR[Err][ib]
	#print y[ib],ex[ib],ey[ib]
    return y,ex,ey

def MakeGraph( Method, Jet, WP, Err, DataPool):
    name = '%s with %s from %s at %s WP of %s'%(Central['title'],Err,Method,WP,Jet)
    lname= '%s with %5s from %s'%(Central['name'],Err,Method)
    NItems = len(XAxis[Jet])
    shift = MethodSet[Method]['shift']*width/(len(ErrSet)*(len(MethodSet)+1))
    binpos = 1.+shift-width/2.+ErrSet[Err]['pos']*width/len(ErrSet)
    x = numpy.ndarray( [NItems] )
    for ib in range( NItems ):
       x[ib] = ib + binpos
       #print x[ib]
    CR = DataPool[Jet][Method][WP]
    y, ex, ey = MakeCentralWithErr( CR, NItems, Err )
    g = TGraphErrors( NItems, x, y, ex, ey )
    g.SetLineWidth(3)

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
