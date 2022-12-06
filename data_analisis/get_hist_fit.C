{		
	Float_t mins1=1000;
	Float_t mins2=1000;
	Float_t maxs1=0;
	Float_t maxs2=0;
	
	Float_t minp1=1000;
	Float_t minp2=1000;
	Float_t maxp1=0;
	Float_t maxp2=0;
	
	Float_t Qs1;
	Float_t Qp1;
	
	Float_t Qs2;
	Float_t Qp2;
	
	Int_t ns;
  	TString filename;
  	TString sufix1;
  	TString sufix2;
  
  	
	ns=120;
  	filename=Form("%dns_pmtbase_T2_noRInDynodes",ns); // no se coloca el .root
	sufix1="_dataI.root";
	sufix2="_Histogram.root";
	
	TFile *f = TFile::Open(filename+sufix1);
	fh = new TFile(filename + sufix2,"recreate");
	
   TTree *t1 = (TTree*)f->Get("tdata_m1");
   TTree *t2 = (TTree*)f->Get("tdata_m2");
   
   
   Double_t random;
   Int_t ev;
   t1->SetBranchAddress("Qs",&Qs1);
   t1->SetBranchAddress("Qp",&Qp1);
   
   t2->SetBranchAddress("Qs",&Qs2);
   t2->SetBranchAddress("Qp",&Qp2);
   
   
   Int_t nentries1 = (Int_t)t1->GetEntries();
   Int_t nentries2 = (Int_t)t2->GetEntries();
   
  
  	
  
  
  	for (Int_t i=0;i<nentries1;i++) {
     t1->GetEntry(i);
     
     if(mins1>Qs1){
     	mins1=Qs1;
     }
     if(maxs1<Qs1){
     	maxs1=Qs1;
     }
     if(minp1>Qp1){
     	minp1=Qp1;
     }
     if(maxp1<Qp1){
		maxp1=Qp1;     
     }
      
 	
   }
 	for (Int_t i=0;i<nentries2;i++) {
     t2->GetEntry(i);
    
     if(mins2>Qs2){
      mins2=Qs2;
     } 
     if(maxs2<Qs2){
      maxs2=Qs2;
     }
     if(minp2>Qp2){
      minp2=Qp2;
     }
     if(maxp2<Qp2){
      maxp2=Qp2;
     }
  }
   
   TH1F *hQs    = new TH1F("hQs" ,"Datos integrados carga Qs"  ,200,mins1-0.5,maxs2+0.5);
   TH1F *hQs1   = new TH1F("hQs1","Datos integrados carga Qs_1",200,mins1-0.5,maxs1+0.5);
   TH1F *hQs2   = new TH1F("hQs2","Datos integrados carga Qs_2",200,mins2-0.5,maxs2+0.5);
   
   TH1F *hQp    = new TH1F("hQp" ,"Datos integrados carga Qp"  ,200,minp1-0.5,maxp2+0.5);
   TH1F *hQp1   = new TH1F("hQp1","Datos integrados carga Qp_1",200,minp1-0.5,maxp1+0.5);
  	TH1F *hQp2   = new TH1F("hQp2","Datos integrados carga Qp_2",200,minp2-0.5,maxp2+0.5);
   
   // all entries and fill the histograms
 
   for (Int_t i=0;i<nentries1;i++) {
     t1->GetEntry(i);
     
     hQs->Fill(Qs1);
     hQp->Fill(Qp1);
     
     hQs1->Fill(Qs1);
     hQp1->Fill(Qp1);
  
  	}
	for (Int_t i=0;i<nentries2;i++) {
     t2->GetEntry(i);
     
     hQs->Fill(Qs2);
     hQp->Fill(Qp2);
     
     hQs2->Fill(Qs2);
     hQp2->Fill(Qp2);
	}	
	
	
	TF1 * fhQs1 = new TF1("fhQs1","gaus(0)");
	TF1 * fhQp1 = new TF1("fhQp1","gaus(0)");
	
	TF1 * fhQs2 = new TF1("fhQs2","gaus(0)");
	TF1 * fhQp2 = new TF1("fhQp2","gaus(0)");
	
	
	hQs1->Fit(fhQs1,"","",mins1-0.5,maxs1+0.5);
	hQp1->Fit(fhQp1,"","",minp1-0.5,maxp1+0.5);
	
	hQs2->Fit(fhQs2,"","",mins2-0.5,maxs2+0.5);
	hQp2->Fit(fhQp2,"","",minp2-0.5,maxp2+0.5);
	
	
	fh->WriteTObject(hQs);
	fh->WriteTObject(hQp);
	
	fh->WriteTObject(hQs1);
	fh->WriteTObject(hQp1);
	
	fh->WriteTObject(hQs2);
	fh->WriteTObject(hQp2);
	

	hQs1->Draw()
   
	
  
  
}
