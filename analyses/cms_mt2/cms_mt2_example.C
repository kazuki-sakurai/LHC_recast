#include "Hemisphere.cc"
#include "Davismt2.cc"
#include <TLorentzVector.h>


extern "C" {

  float getMT2(int njet, double px_jets[], double py_jets[], double pz_jets[], double E_jets[], double METx, double METy){

    //cout <<"px_car[1]  "<< px_jets[1] << endl;

    // options
    int hemi_seed=2;        // seeding method, 2: max inv mass
    int hemi_association=3; // association method, 3: minimal lund distance
    bool massive=false;     // use massles pseudo jets
    
    vector<float> px, py, pz, E; // jets 4-momenta

    ////// REPLACE jets and MET vectors    
    // TLorentzVector jet1;
    // jet1.SetPtEtaPhiM(181.18336,1.6536277,-0.557520,15.047922);
    // TLorentzVector jet2;
    // jet2.SetPtEtaPhiM(97.920494,0.7973791,-0.566087,9.8400964);
    
    TLorentzVector MET;
    //MET.SetPtEtaPhiM(305.92797,0.,2.5043566,0.);
    double METmag = pow(METx*METx + METy*METy, 0.5);
    MET.SetPxPyPzE(METx,METy,0.,METmag);

    //////

    //fill jets
    for(int i=0; i<njet; i++){
        px.push_back(px_jets[i]);
        py.push_back(py_jets[i]);
        pz.push_back(pz_jets[i]);
        E.push_back(E_jets[i]);
    }
    
    // get hemispheres
    Hemisphere* hemisp = new Hemisphere(px, py, pz, E, hemi_seed, hemi_association);
    vector<int> grouping = hemisp->getGrouping();
    
    TLorentzVector pseudojet1(0.,0.,0.,0.);
    TLorentzVector pseudojet2(0.,0.,0.,0.);
    
    for(int i=0; i<px.size(); ++i){
      if(grouping[i]==1){
        pseudojet1.SetPx(pseudojet1.Px() + px[i]);
        pseudojet1.SetPy(pseudojet1.Py() + py[i]);
        pseudojet1.SetPz(pseudojet1.Pz() + pz[i]);
        pseudojet1.SetE (pseudojet1.E () + E [i]);   
      }else if(grouping[i] == 2){
        pseudojet2.SetPx(pseudojet2.Px() + px[i]);
        pseudojet2.SetPy(pseudojet2.Py() + py[i]);
        pseudojet2.SetPz(pseudojet2.Pz() + pz[i]);
        pseudojet2.SetE (pseudojet2.E () + E [i]);
      }
    }
    
    // ingredients for MT2
    double pa[3];
    double pb[3];
    double pmiss[3];
    
    pmiss[0] = 0;
    pmiss[1] = static_cast<double> (MET.Px());
    pmiss[2] = static_cast<double> (MET.Py());
    
    pa[0] = static_cast<double> (massive ? pseudojet1.M() : 0);
    pa[1] = static_cast<double> (pseudojet1.Px());
    pa[2] = static_cast<double> (pseudojet1.Py());
    
    pb[0] = static_cast<double> (massive ? pseudojet2.M() : 0);
    pb[1] = static_cast<double> (pseudojet2.Px());
    pb[2] = static_cast<double> (pseudojet2.Py());
    

    //set test mass equal to zero
    float testmass=0.0;

    //get MT2
    Davismt2 *mt2 = new Davismt2();
    mt2->set_momenta(pa, pb, pmiss);
    mt2->set_mn(testmass);

    float MT2=mt2->get_mt2();

    //cout << "MT2 in C++: " << MT2 << endl; 
    
    return MT2;

  }

}

// void fullExample(){
//   std::cout << "start 1" << std::endl;
//   float MT2 = getMT2();
//   std::cout << MT2 << std::endl;
// }