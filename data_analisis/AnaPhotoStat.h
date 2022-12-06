//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Nov 11 11:43:27 2022 by ROOT version 6.26/04
// from TTree oscdata/osciloscope data
// found on file: 20ns_pmtbase_T2_noRInDynodes.root
//////////////////////////////////////////////////////////

#ifndef AnaPhotoStat_h
#define AnaPhotoStat_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include "TH1D.h"
#include "TObject.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TNtuple.h"
#include "TString.h"

// Header file for the classes stored in the TTree if any.

class AnaPhotoStat {
public :
  TTree          *fChain;   //!pointer to the analyzed TTree or TChain
  Int_t           fCurrent; //!current Tree number in a TChain
  TFile *ofile;
  TString fname = "dataI.root";
  TString prefix = "";
  // Fixed size dimensions of array or collections stored in the TTree if any.

  // Declaration of leaf types
  Float_t evn;
  Float_t t;
  Float_t v0;
  Float_t v1;
  Float_t v2;
  
  //variables
  Float_t ped0;
  Float_t ped2;
  Float_t signal;
  Float_t pulse;
  Float_t delta_t;
  Float_t min1;
  Float_t min2;
  Float_t evn_min; 
  
  //temporals
  Float_t temp_m;
  Float_t temp_rt;
  Float_t temp_t;
  
  //counts
  Int_t cnt_ped;
  Int_t cnt_signal;
  Int_t cnt_pulse;
  Int_t curr_evn;
  Int_t cnt_rt;
  Int_t cnt_t;

  const Float_t TMIN_PED0 = -0.1e-6;
  const Float_t TMAX_PED0 = -0.02e-6;
  const Float_t TMIN_SIGNAL = 0.05e-6;
  const Float_t TMAX_SIGNAL= 0.3e-6;
  const Float_t TMIN_PULSE = -0.05e-6;
  const Float_t TMAX_PULSE= 0.2e-6;
  const Float_t time_var=0.5e-8;
  const Float_t volt_var=0.05;
  
  Float_t QS1[1650];
  Float_t QP1[1650];
  Float_t QS2[1650];
  Float_t QP2[1650];
  
  Float_t return_t[1650];
  
  TH1D *hQs;
  TH1D *hQp;
  TH1D *hQs1;
  TH1D *hQp1;
  TH1D *hQs2;
  TH1D *hQp2;
  
  TH1D *hDt;
  TNtuple *tdata_t;
  TNtuple *tdata_m1;
  TNtuple *tdata_m2;
  
  // List of branches
  TBranch        *b_evn;   //!
  TBranch        *b_t;   //!
  TBranch        *b_v0;   //!
  TBranch        *b_v1;   //!
  TBranch        *b_v2;   //!

  AnaPhotoStat(TTree *tree=0,TString pf = "");
  virtual ~AnaPhotoStat();
  virtual Int_t    Cut(Long64_t entry);
  virtual Int_t    GetEntry(Long64_t entry);
  virtual Long64_t LoadTree(Long64_t entry);
  virtual void     Init(TTree *tree);
  virtual Int_t    FillData();
  virtual void    Loop();
  virtual Bool_t   Notify();
  virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef AnaPhotoStat_cxx
AnaPhotoStat::AnaPhotoStat(TTree *tree, TString pf) : fChain(0) 
{
  prefix = pf;
  // if parameter tree is not specified (or zero), connect the file
  // used to generate this class and read the Tree.
  if (tree == 0) {
    TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("20ns_pmtbase_T2_noRInDynodes.root");
    if (!f || !f->IsOpen()) {
      f = new TFile("20ns_pmtbase_T2_noRInDynodes.root");
    }
    f->GetObject("oscdata",tree);

  }
  Init(tree);
}

AnaPhotoStat::~AnaPhotoStat()
{
  if (!fChain) return;
  delete fChain->GetCurrentFile();
}

Int_t AnaPhotoStat::GetEntry(Long64_t entry)
{
  // Read contents of entry.
  if (!fChain) return 0;
  return fChain->GetEntry(entry);
}
Long64_t AnaPhotoStat::LoadTree(Long64_t entry)
{
  // Set the environment to read one entry
  if (!fChain) return -5;
  Long64_t centry = fChain->LoadTree(entry);
  if (centry < 0) return centry;
  if (fChain->GetTreeNumber() != fCurrent) {
    fCurrent = fChain->GetTreeNumber();
    Notify();
  }
  return centry;
}

void AnaPhotoStat::Init(TTree *tree)
{
  // The Init() function is called when the selector needs to initialize
  // a new tree or chain. Typically here the branch addresses and branch
  // pointers of the tree will be set.
  // It is normally not necessary to make changes to the generated
  // code, but the routine can be extended by the user if needed.
  // Init() will be called many times when running on PROOF
  // (once per file to be processed).

  // Set branch addresses and branch pointers
  if (!tree) return;
  fChain = tree;
  fCurrent = -1;
  fChain->SetMakeClass(1);

  fChain->SetBranchAddress("evn", &evn, &b_evn);
  fChain->SetBranchAddress("t", &t, &b_t);
  fChain->SetBranchAddress("v0", &v0, &b_v0);
  fChain->SetBranchAddress("v1", &v1, &b_v1);
  fChain->SetBranchAddress("v2", &v2, &b_v2);
  
  ofile = new TFile(prefix + fname,"recreate");
  
  //hQs = new TH1D("hQs","Charge Histogram",200,-1,4);
  //hQp = new TH1D("hQp","Charge Histogram",200,25,65);
  //hQs1 = new TH1D("hQs1","Charge Histogram",200,-1,4);
  //hQp1 = new TH1D("hQp1","Charge Histogram",200,25,65);
  //hQs2 = new TH1D("hQs2","Charge Histogram",200,-1,4);
  //hQp2 = new TH1D("hQp2","Charge Histogram",200,25,65);
  
  tdata_t  = new TNtuple("tdata_t","Total datos integrados","Qs:Qp");
  tdata_m1 = new TNtuple("tdata_m1","datos integrados para un tipo de pulso","Qs:Qp");
  tdata_m2 = new TNtuple("tdata_m2","datos integrados para un tipo de pulso","Qs:Qp");

  hDt = new TH1D("hDt","Delta t",150,0,0.8e-6);
          
  Notify();
}

Bool_t AnaPhotoStat::Notify()
{
  // The Notify() function is called when a new file is opened. This
  // can be either for a new TTree in a TChain or when when a new TTree
  // is started when using PROOF. It is normally not necessary to make changes
  // to the generated code, but the routine can be extended by the
// user if needed. The return value is currently not used.

  return kTRUE;
}

void AnaPhotoStat::Show(Long64_t entry)
{
  // Print contents of entry.
  // If entry is not specified, print current entry
  if (!fChain) return;
  fChain->Show(entry);
}
Int_t AnaPhotoStat::Cut(Long64_t entry)
{
  // This function may be called from Loop.
  // returns  1 if entry is accepted.
  // returns -1 otherwise.
  return 1;
}
#endif // #ifdef AnaPhotoStat_cxx
